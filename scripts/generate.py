#!/usr/bin/env python3
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "build" / "generated"
GEN.mkdir(parents=True, exist_ok=True)

GANA_NAMES = {
1:("भ्वादिगणः","bhvādi"),2:("अदादिगणः","adādi"),3:("जुहोत्यादिगणः","juhotyādi"),
4:("दिवादिगणः","divādi"),5:("स्वादिगणः","svādi"),6:("तुदादिगणः","tudādi"),
7:("रुधादिगणः","rudhādi"),8:("तनादिगणः","tanādi"),9:("क्र्यादिगणः","kryādi"),
10:("चुरादिगणः","curādi"),11:("कण्ड्वादिगणः","kaṇḍvādi")}

def esc(s):
    return s.replace("\\","\\textbackslash{}").replace("&","\\&").replace("%","\\%").replace("_","\\_").replace("#","\\#")

def load_json(name):
    return json.loads((ROOT/"data"/name).read_text(encoding="utf-8"))

def generate_dhatupatha():
    path=ROOT/"data/dhatupatha.tsv"
    if not path.exists(): raise SystemExit("Run scripts/fetch_dhatupatha.py first.")
    groups={i:[] for i in range(1,12)}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            try: g=int(row["code"].split(".")[0])
            except Exception: continue
            if g in groups: groups[g].append(row)
    out=[r"\chapter{\SA{सम्पूर्णधातुपाठः}}","The source rows are printed without silently removing indicatory markers.",r"\begin{longtable}{p{.12\linewidth}p{.22\linewidth}p{.58\linewidth}}",r"\toprule Code & Dhātu (SLP1) & Artha (SLP1)\\\midrule\endhead"]
    for g in range(1,12):
        sa,roman=GANA_NAMES[g]
        out += [rf"\multicolumn{{3}}{{l}}{{\EmptyTarget{{gana:{g:02d}}}\textbf{{\SA{{{sa}}} — {roman}}}}}\\",r"\midrule"]
        for row in groups[g]:
            rid="DHATU-"+row["code"].replace(".","-")
            out.append(rf"\EmptyTarget{{root:{rid}}}\texttt{{{esc(row['code'])}}} & \texttt{{{esc(row['dhatu'])}}} & \texttt{{{esc(row['artha'])}}}\\")
        out.append(r"\addlinespace")
    out += [r"\bottomrule\end{longtable}"]
    (GEN/"dhatupatha.tex").write_text("\n".join(out),encoding="utf-8")

def rule_key(num): return tuple(int(x) for x in num.split("."))

def generate_rules():
    out=[r"\chapter{\SA{क्रमेण सूत्रपञ्जी}}","Rules are sorted numerically. The registry distinguishes the sūtra text, its local operational use, and its audit status."]
    for r in sorted(load_json("rules.json"),key=lambda x:rule_key(x["number"])):
        out += [rf"\section{{\EmptyTarget{{rule:{r['id']}}}{r['number']} — \SA{{{r['sutra']}}}}}",rf"\textbf{{Scope:}} {esc(r['scope'])}. \textbf{{Status:}} {esc(r['status'])}.",esc(r["operation"])]
    (GEN/"rules.tex").write_text("\n\n".join(out),encoding="utf-8")

def generate_categories():
    cats,ex=load_json("categories.json"),load_json("examples.json")
    out=[r"\chapter{\SA{रचनावर्गाः} — categories of composition}"]
    for cid,c in cats.items():
        out += [rf"\section{{\EmptyTarget{{category:{cid}}}\SA{{{c['name']}}}}}",esc(c["description"])]
        roots=[e for e in ex if cid in e["category"]]
        if roots:
            out.append(r"\begin{itemize}")
            out += [rf"\item \SA{{{e['root']} → {e['kta']}}} (\texttt{{{esc(e['code'])}}})" for e in roots]
            out.append(r"\end{itemize}")
    (GEN/"categories.tex").write_text("\n".join(out),encoding="utf-8")

def generate_irregular():
    ex=load_json("examples.json"); out=[r"\chapter{\SA{गणशः अनियमितनिर्माणदृष्टान्ताः}}"]
    for g in range(1,12):
        sa,_=GANA_NAMES[g]; out.append(rf"\section{{\SA{{{sa}}}}}")
        rows=[e for e in ex if e["gana"]==g and ("CAT-LEXICAL" in e["category"] or "CAT-OPTIONAL" in e["category"])]
        if not rows: out.append("No audited irregular example entered yet.")
        for e in rows:
            out += [rf"\EmptyTarget{{deriv:G{g:02d}-{e['code']}-KTA}}\SA{{{e['root']} → {e['kta']}}}. {esc(e['note'])}","Rules: "+", ".join(rf"\RuleRef{{{x}}}" for x in e["rules"])]
    (GEN/"irregular.tex").write_text("\n".join(out),encoding="utf-8")

def generate_audit():
    out=[r"\begin{longtable}{p{.12\linewidth}p{.16\linewidth}p{.18\linewidth}p{.45\linewidth}}",r"\toprule Gaṇa & Root & kta & Status note\\\midrule\endhead"]
    for e in load_json("examples.json"):
        out.append(rf"{e['gana']} & \SA{{{e['root']}}} & \SA{{{e['kta']}}} & {esc(e['note'])}\\")
    out += [r"\bottomrule\end{longtable}"]
    (GEN/"audit.tex").write_text("\n".join(out),encoding="utf-8")

def main():
    generate_dhatupatha(); generate_rules(); generate_categories(); generate_irregular(); generate_audit()
    print("Generated LaTeX registries in", GEN)

if __name__=="__main__": main()
