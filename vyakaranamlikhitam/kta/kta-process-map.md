<a id="toc"></a>
# <span lang="sa-Deva">क्तप्रक्रियामानचित्रम्</span> — the linked *⟨kta⟩* process map

A long-term, generator-backed map for deciding and deriving the Sanskrit *⟨kta⟩* form. Sanskrit is marked as italic IAST; Devanāgarī is supplied where it preserves the source text most clearly. Verbal roots carry `√`, and affixes are enclosed in `⟨ ⟩`.

## Table of contents

- [Bar-down process preamble](#process-map)
- [Preamble 1 — *dhātu-gaṇāḥ*: complete Dhātupāṭha](#preamble-1)
  - [Gaṇa 1: bhvādi-gaṇaḥ](#gana-01)
  - [Gaṇa 2: adādi-gaṇaḥ](#gana-02)
  - [Gaṇa 3: juhotyādi-gaṇaḥ](#gana-03)
  - [Gaṇa 4: divādi-gaṇaḥ](#gana-04)
  - [Gaṇa 5: svādi-gaṇaḥ](#gana-05)
  - [Gaṇa 6: tudādi-gaṇaḥ](#gana-06)
  - [Gaṇa 7: rudhādi-gaṇaḥ](#gana-07)
  - [Gaṇa 8: tanādi-gaṇaḥ](#gana-08)
  - [Gaṇa 9: kryādi-gaṇaḥ](#gana-09)
  - [Gaṇa 10: curādi-gaṇaḥ](#gana-10)
  - [Gaṇa 11: kaṇḍvādi-gaṇaḥ](#gana-11)
- [Preamble 2 — *sūtrāṇi*: ordered rule registry](#preamble-2)
- [Chapter 1: bhvādi-gaṇaḥ-padam](#chapter-01)
- [Chapter 2: adādi-gaṇaḥ-padam](#chapter-02)
- [Chapter 3: juhotyādi-gaṇaḥ-padam](#chapter-03)
- [Chapter 4: divādi-gaṇaḥ-padam](#chapter-04)
- [Chapter 5: svādi-gaṇaḥ-padam](#chapter-05)
- [Chapter 6: tudādi-gaṇaḥ-padam](#chapter-06)
- [Chapter 7: rudhādi-gaṇaḥ-padam](#chapter-07)
- [Chapter 8: tanādi-gaṇaḥ-padam](#chapter-08)
- [Chapter 9: kryādi-gaṇaḥ-padam](#chapter-09)
- [Chapter 10: curādi-gaṇaḥ-padam](#chapter-10)
- [Chapter 11: kaṇḍvādi-gaṇaḥ-padam](#chapter-11)
- [Sandhi rules employed](#sandhi-registry)
- [Categories of composition](#composition-categories)
- [Irregular constructions by gaṇa](#irregular-by-gana)
- [Sources and generation contract](#sources)

<a id="process-map"></a>
## Bar-down process preamble

| Bar | Decision | Registry destination |
|---|---|---|
| **B0 — identity** | Resolve the exact Dhātupāṭha entry, gaṇa, indicatory markers, meaning, preverb, and intended syntax. | [Preamble 1](#preamble-1) |
| **B1 — affix** | Introduce *⟨kta⟩* and register it as *niṣṭhā*. | [AS-1-1-26](#rule-as-1-1-26); [AS-3-2-102](#rule-as-3-2-102) |
| **B2 — interpretation** | Test the ordinary resultative/passive reading and any licensed *kartari* interpretation. | [AS-3-4-72](#rule-as-3-4-72) |
| **B3 — iṭ** | Apply the ārdhadhātuka *iṭ* system; do not infer *seṭ / aniṭ / veṭ* from gaṇa alone. | [AS-7-2-35](#rule-as-7-2-35) |
| **B4 — root operations** | Apply substitutions, augments, and ordered phonology, recording every invoked rule once locally. | [Preamble 2](#preamble-2) |
| **B5 — niṣṭhā** | Search 8.2.42ff. for substitution, lexical prescription, option, prohibition, or meaning-conditioned output. | [AS-8-2-42](#rule-as-8-2-42) |
| **B6 — sandhi** | Apply only rules actually triggered by the derivation. | [Sandhi registry](#sandhi-registry) |
| **B7 — audit** | Return the surface form, competing licensed forms, interpretation, sources, and unresolved commentarial questions. | [Categories](#composition-categories) |

### Gaṇa chapter map

| Gaṇa | Dhātupāṭha registry | Derivation chapter | Entries |
|---:|---|---|---:|
| 1 | [<i lang="sa-Latn">bhvādi-gaṇaḥ</i> · <span lang="sa-Deva">भ्वादिगणः</span>](#gana-01) | [chapter 1](#chapter-01) | 1166 |
| 2 | [<i lang="sa-Latn">adādi-gaṇaḥ</i> · <span lang="sa-Deva">अदादिगणः</span>](#gana-02) | [chapter 2](#chapter-02) | 77 |
| 3 | [<i lang="sa-Latn">juhotyādi-gaṇaḥ</i> · <span lang="sa-Deva">जुहोत्यादिगणः</span>](#gana-03) | [chapter 3](#chapter-03) | 26 |
| 4 | [<i lang="sa-Latn">divādi-gaṇaḥ</i> · <span lang="sa-Deva">दिवादिगणः</span>](#gana-04) | [chapter 4](#chapter-04) | 163 |
| 5 | [<i lang="sa-Latn">svādi-gaṇaḥ</i> · <span lang="sa-Deva">स्वादिगणः</span>](#gana-05) | [chapter 5](#chapter-05) | 38 |
| 6 | [<i lang="sa-Latn">tudādi-gaṇaḥ</i> · <span lang="sa-Deva">तुदादिगणः</span>](#gana-06) | [chapter 6](#chapter-06) | 174 |
| 7 | [<i lang="sa-Latn">rudhādi-gaṇaḥ</i> · <span lang="sa-Deva">रुधादिगणः</span>](#gana-07) | [chapter 7](#chapter-07) | 25 |
| 8 | [<i lang="sa-Latn">tanādi-gaṇaḥ</i> · <span lang="sa-Deva">तनादिगणः</span>](#gana-08) | [chapter 8](#chapter-08) | 10 |
| 9 | [<i lang="sa-Latn">kryādi-gaṇaḥ</i> · <span lang="sa-Deva">क्र्यादिगणः</span>](#gana-09) | [chapter 9](#chapter-09) | 71 |
| 10 | [<i lang="sa-Latn">curādi-gaṇaḥ</i> · <span lang="sa-Deva">चुरादिगणः</span>](#gana-10) | [chapter 10](#chapter-10) | 509 |
| 11 | [<i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i> · <span lang="sa-Deva">कण्ड्वादिगणः</span>](#gana-11) | [chapter 11](#chapter-11) | 1 |

[↑ Contents](#toc)

<a id="preamble-1"></a>
# Preamble 1 — <i lang="sa-Latn">dhātu-gaṇāḥ</i>: complete Dhātupāṭha

The source rows are reproduced in gaṇa order without silently removing indicatory markers. Each entry has a stable anchor for chapter derivations.

<a id="gana-01"></a>
## Gaṇa 1 — <i lang="sa-Latn">bhvādi-gaṇaḥ</i> · <span lang="sa-Deva">भ्वादिगणः</span>

[Derivation chapter 1](#chapter-01) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-01-0001"></a>`01.0001` | <i lang="sa-Latn">√bhū</i> | <i lang="sa-Latn">sattāyām</i> |
| <a id="dhatu-01-0002"></a>`01.0002` | <i lang="sa-Latn">√edha~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0003"></a>`01.0003` | <i lang="sa-Latn">√spardha~\</i> | <i lang="sa-Latn">saṅgharṣe</i> |
| <a id="dhatu-01-0004"></a>`01.0004` | <i lang="sa-Latn">√gādhṛ~\</i> | <i lang="sa-Latn">pratiṣṭhālipsayorgranthe ca</i> |
| <a id="dhatu-01-0005"></a>`01.0005` | <i lang="sa-Latn">√bādhṛ~\</i> | <i lang="sa-Latn">loḍane, roṭane</i> |
| <a id="dhatu-01-0006"></a>`01.0006` | <i lang="sa-Latn">√nādhṛ~\</i> | <i lang="sa-Latn">yācñopatāpaiśvaryāśīṣṣu</i> |
| <a id="dhatu-01-0007"></a>`01.0007` | <i lang="sa-Latn">√nāthṛ~\</i> | <i lang="sa-Latn">yācñopatāpaiśvaryāśīṣṣu</i> |
| <a id="dhatu-01-0008"></a>`01.0008` | <i lang="sa-Latn">√dadha~\</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-01-0009"></a>`01.0009` | <i lang="sa-Latn">√skudi~\</i> | <i lang="sa-Latn">āpravaṇe</i> |
| <a id="dhatu-01-0010"></a>`01.0010` | <i lang="sa-Latn">√śvidi~\</i> | <i lang="sa-Latn">śvaitye</i> |
| <a id="dhatu-01-0011"></a>`01.0011` | <i lang="sa-Latn">√vadi~\</i> | <i lang="sa-Latn">abhivādanastutyoḥ</i> |
| <a id="dhatu-01-0012"></a>`01.0012` | <i lang="sa-Latn">√bhadi~\</i> | <i lang="sa-Latn">kalyāṇe sukhe ca</i> |
| <a id="dhatu-01-0013"></a>`01.0013` | <i lang="sa-Latn">√madi~\</i> | <i lang="sa-Latn">stutimodamadasvapnakāntigatiṣu</i> |
| <a id="dhatu-01-0014"></a>`01.0014` | <i lang="sa-Latn">√spadi~\</i> | <i lang="sa-Latn">kiñciccalane</i> |
| <a id="dhatu-01-0015"></a>`01.0015` | <i lang="sa-Latn">√klidi~\</i> | <i lang="sa-Latn">paridevane</i> |
| <a id="dhatu-01-0016"></a>`01.0016` | <i lang="sa-Latn">√muda~\</i> | <i lang="sa-Latn">harṣe</i> |
| <a id="dhatu-01-0017"></a>`01.0017` | <i lang="sa-Latn">√dada~\</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-01-0018"></a>`01.0018` | <i lang="sa-Latn">√ṣvada~\</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-01-0019"></a>`01.0019` | <i lang="sa-Latn">√svarda~\</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-01-0020"></a>`01.0020` | <i lang="sa-Latn">√urda~\</i> | <i lang="sa-Latn">māne krīḍāyāṃ āsvādane ca</i> |
| <a id="dhatu-01-0021"></a>`01.0021` | <i lang="sa-Latn">√kurda~\</i> | <i lang="sa-Latn">krīḍāyām eva</i> |
| <a id="dhatu-01-0022"></a>`01.0022` | <i lang="sa-Latn">√khurda~\</i> | <i lang="sa-Latn">krīḍāyām eva</i> |
| <a id="dhatu-01-0023"></a>`01.0023` | <i lang="sa-Latn">√gurda~\</i> | <i lang="sa-Latn">krīḍāyām eva</i> |
| <a id="dhatu-01-0024"></a>`01.0024` | <i lang="sa-Latn">√guda~\</i> | <i lang="sa-Latn">krīḍāyām eva</i> |
| <a id="dhatu-01-0025"></a>`01.0025` | <i lang="sa-Latn">√ṣūda~\</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-01-0026"></a>`01.0026` | <i lang="sa-Latn">√hrāda~\</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0027"></a>`01.0027` | <i lang="sa-Latn">√hlādī~\</i> | <i lang="sa-Latn">avyakte śabde sukhe ca</i> |
| <a id="dhatu-01-0028"></a>`01.0028` | <i lang="sa-Latn">√svāda~\</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-01-0029"></a>`01.0029` | <i lang="sa-Latn">√parda~\</i> | <i lang="sa-Latn">kutsite śabde</i> |
| <a id="dhatu-01-0030"></a>`01.0030` | <i lang="sa-Latn">√yatī~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0031"></a>`01.0031` | <i lang="sa-Latn">√yutṛ~\</i> | <i lang="sa-Latn">bhāsane</i> |
| <a id="dhatu-01-0032"></a>`01.0032` | <i lang="sa-Latn">√jutṛ~\</i> | <i lang="sa-Latn">bhāsane</i> |
| <a id="dhatu-01-0033"></a>`01.0033` | <i lang="sa-Latn">√vithṛ~\</i> | <i lang="sa-Latn">yācane</i> |
| <a id="dhatu-01-0034"></a>`01.0034` | <i lang="sa-Latn">√vethṛ~\</i> | <i lang="sa-Latn">yācane</i> |
| <a id="dhatu-01-0035"></a>`01.0035` | <i lang="sa-Latn">√śrathi~\</i> | <i lang="sa-Latn">śaithilye</i> |
| <a id="dhatu-01-0036"></a>`01.0036` | <i lang="sa-Latn">√grathi~\</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-01-0037"></a>`01.0037` | <i lang="sa-Latn">√kattha~\</i> | <i lang="sa-Latn">ślāghāyām</i> |
| <a id="dhatu-01-0038"></a>`01.0038` | <i lang="sa-Latn">√ata~</i> | <i lang="sa-Latn">sātatyagamane</i> |
| <a id="dhatu-01-0039"></a>`01.0039` | <i lang="sa-Latn">√citī~</i> | <i lang="sa-Latn">saṃjñāne</i> |
| <a id="dhatu-01-0040"></a>`01.0040` | <i lang="sa-Latn">√cyuti~r</i> | <i lang="sa-Latn">āsecane</i> |
| <a id="dhatu-01-0041"></a>`01.0041` | <i lang="sa-Latn">√ścuti~r</i> | <i lang="sa-Latn">āsecane</i> |
| <a id="dhatu-01-0042"></a>`01.0042` | <i lang="sa-Latn">√ścyuti~r</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-01-0043"></a>`01.0043` | <i lang="sa-Latn">√jyutṛ~</i> | <i lang="sa-Latn">bhāsane</i> |
| <a id="dhatu-01-0044"></a>`01.0044` | <i lang="sa-Latn">√mathi~</i> | <i lang="sa-Latn">hiṃsāsaṅkleśanayoḥ</i> |
| <a id="dhatu-01-0045"></a>`01.0045` | <i lang="sa-Latn">√kuthi~</i> | <i lang="sa-Latn">hiṃsāsaṅkleśanayoḥ</i> |
| <a id="dhatu-01-0046"></a>`01.0046` | <i lang="sa-Latn">√puthi~</i> | <i lang="sa-Latn">hiṃsāsaṅkleśanayoḥ</i> |
| <a id="dhatu-01-0047"></a>`01.0047` | <i lang="sa-Latn">√luthi~</i> | <i lang="sa-Latn">hiṃsāsaṅkleśanayoḥ</i> |
| <a id="dhatu-01-0048"></a>`01.0048` | <i lang="sa-Latn">√mantha~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-01-0049"></a>`01.0049` | <i lang="sa-Latn">√ṣidha~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-01-0050"></a>`01.0050` | <i lang="sa-Latn">√ṣidhū~</i> | <i lang="sa-Latn">śāstre (śāsane) māṅgalye ca</i> |
| <a id="dhatu-01-0051"></a>`01.0051` | <i lang="sa-Latn">√khādṛ~</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-01-0052"></a>`01.0052` | <i lang="sa-Latn">√khada~</i> | <i lang="sa-Latn">sthairye hiṃsāyāṃ bhakṣaṇe ca</i> |
| <a id="dhatu-01-0053"></a>`01.0053` | <i lang="sa-Latn">√bada~</i> | <i lang="sa-Latn">sthairye</i> |
| <a id="dhatu-01-0054"></a>`01.0054` | <i lang="sa-Latn">√gada~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0055"></a>`01.0055` | <i lang="sa-Latn">√rada~</i> | <i lang="sa-Latn">vilekhane</i> |
| <a id="dhatu-01-0056"></a>`01.0056` | <i lang="sa-Latn">√ṇada~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0057"></a>`01.0057` | <i lang="sa-Latn">√arda~</i> | <i lang="sa-Latn">gatau yācane ca</i> |
| <a id="dhatu-01-0058"></a>`01.0058` | <i lang="sa-Latn">√narda~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0059"></a>`01.0059` | <i lang="sa-Latn">√garda~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0060"></a>`01.0060` | <i lang="sa-Latn">√tarda~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0061"></a>`01.0061` | <i lang="sa-Latn">√karda~</i> | <i lang="sa-Latn">kutsite śabde</i> |
| <a id="dhatu-01-0062"></a>`01.0062` | <i lang="sa-Latn">√kharda~</i> | <i lang="sa-Latn">dandaśūke (sarpadaṃśe)</i> |
| <a id="dhatu-01-0063"></a>`01.0063` | <i lang="sa-Latn">√ati~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0064"></a>`01.0064` | <i lang="sa-Latn">√adi~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0065"></a>`01.0065` | <i lang="sa-Latn">√idi~</i> | <i lang="sa-Latn">paramaiśvarye</i> |
| <a id="dhatu-01-0066"></a>`01.0066` | <i lang="sa-Latn">√bidi~</i> | <i lang="sa-Latn">avayave</i> |
| <a id="dhatu-01-0067"></a>`01.0067` | <i lang="sa-Latn">√bhidi~</i> | <i lang="sa-Latn">avayave</i> |
| <a id="dhatu-01-0068"></a>`01.0068` | <i lang="sa-Latn">√gaḍi~</i> | <i lang="sa-Latn">vadanaikadeśe</i> |
| <a id="dhatu-01-0069"></a>`01.0069` | <i lang="sa-Latn">√ṇidi~</i> | <i lang="sa-Latn">kutsāyām</i> |
| <a id="dhatu-01-0070"></a>`01.0070` | <i lang="sa-Latn">√ṭunadi~</i> | <i lang="sa-Latn">samṛddhau</i> |
| <a id="dhatu-01-0071"></a>`01.0071` | <i lang="sa-Latn">√cadi~</i> | <i lang="sa-Latn">āhlāde dīptau ca</i> |
| <a id="dhatu-01-0072"></a>`01.0072` | <i lang="sa-Latn">√tradi~</i> | <i lang="sa-Latn">ceṣṭāyām</i> |
| <a id="dhatu-01-0073"></a>`01.0073` | <i lang="sa-Latn">√kadi~</i> | <i lang="sa-Latn">āhvāne rodane ca</i> |
| <a id="dhatu-01-0074"></a>`01.0074` | <i lang="sa-Latn">√kradi~</i> | <i lang="sa-Latn">āhvāne rodane ca</i> |
| <a id="dhatu-01-0075"></a>`01.0075` | <i lang="sa-Latn">√kladi~</i> | <i lang="sa-Latn">āhvāne rodane ca</i> |
| <a id="dhatu-01-0076"></a>`01.0076` | <i lang="sa-Latn">√klidi~</i> | <i lang="sa-Latn">paridevane</i> |
| <a id="dhatu-01-0077"></a>`01.0077` | <i lang="sa-Latn">√śundha~</i> | <i lang="sa-Latn">śuddhau</i> |
| <a id="dhatu-01-0078"></a>`01.0078` | <i lang="sa-Latn">√śīkṛ~\</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0079"></a>`01.0079` | <i lang="sa-Latn">√sīkṛ~\</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0080"></a>`01.0080` | <i lang="sa-Latn">√lokṛ~\</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-01-0081"></a>`01.0081` | <i lang="sa-Latn">√ślokṛ~\</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0082"></a>`01.0082` | <i lang="sa-Latn">√śrekṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0083"></a>`01.0083` | <i lang="sa-Latn">√drekṛ~\</i> | <i lang="sa-Latn">śabdotsāhayoḥ</i> |
| <a id="dhatu-01-0084"></a>`01.0084` | <i lang="sa-Latn">√dhrekṛ~\</i> | <i lang="sa-Latn">śabdotsāhayoḥ</i> |
| <a id="dhatu-01-0085"></a>`01.0085` | <i lang="sa-Latn">√rekṛ~\</i> | <i lang="sa-Latn">śaṅkāyām</i> |
| <a id="dhatu-01-0086"></a>`01.0086` | <i lang="sa-Latn">√sekṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0087"></a>`01.0087` | <i lang="sa-Latn">√srekṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0088"></a>`01.0088` | <i lang="sa-Latn">√sraki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0089"></a>`01.0089` | <i lang="sa-Latn">√śraki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0090"></a>`01.0090` | <i lang="sa-Latn">√ślaki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0091"></a>`01.0091` | <i lang="sa-Latn">√śaki~\</i> | <i lang="sa-Latn">śaṅkāyām</i> |
| <a id="dhatu-01-0092"></a>`01.0092` | <i lang="sa-Latn">√aki~\</i> | <i lang="sa-Latn">lakṣaṇe</i> |
| <a id="dhatu-01-0093"></a>`01.0093` | <i lang="sa-Latn">√vaki~\</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-01-0094"></a>`01.0094` | <i lang="sa-Latn">√maki~\</i> | <i lang="sa-Latn">maṇḍane</i> |
| <a id="dhatu-01-0095"></a>`01.0095` | <i lang="sa-Latn">√kaka~\</i> | <i lang="sa-Latn">laulye</i> |
| <a id="dhatu-01-0096"></a>`01.0096` | <i lang="sa-Latn">√kuka~\</i> | <i lang="sa-Latn">ādāne</i> |
| <a id="dhatu-01-0097"></a>`01.0097` | <i lang="sa-Latn">√vṛka~\</i> | <i lang="sa-Latn">ādāne</i> |
| <a id="dhatu-01-0098"></a>`01.0098` | <i lang="sa-Latn">√caka~\</i> | <i lang="sa-Latn">tṛptau pratīghāte ca</i> |
| <a id="dhatu-01-0099"></a>`01.0099` | <i lang="sa-Latn">√kaki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0100"></a>`01.0100` | <i lang="sa-Latn">√vaki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0101"></a>`01.0101` | <i lang="sa-Latn">√śvaki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0102"></a>`01.0102` | <i lang="sa-Latn">√traki~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0103"></a>`01.0103` | <i lang="sa-Latn">√ḍhaukṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0104"></a>`01.0104` | <i lang="sa-Latn">√traukṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0105"></a>`01.0105` | <i lang="sa-Latn">√ṣvaṣka~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0106"></a>`01.0106` | <i lang="sa-Latn">√vaska~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0107"></a>`01.0107` | <i lang="sa-Latn">√maska~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0108"></a>`01.0108` | <i lang="sa-Latn">√ṭikṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0109"></a>`01.0109` | <i lang="sa-Latn">√ṭīkṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0110"></a>`01.0110` | <i lang="sa-Latn">√tikṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0111"></a>`01.0111` | <i lang="sa-Latn">√tīkṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0112"></a>`01.0112` | <i lang="sa-Latn">√raghi~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0113"></a>`01.0113` | <i lang="sa-Latn">√laghi~\</i> | <i lang="sa-Latn">gatau bhojananivṛttau ca</i> |
| <a id="dhatu-01-0114"></a>`01.0114` | <i lang="sa-Latn">√ṣvakka~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0115"></a>`01.0115` | <i lang="sa-Latn">√aghi~\</i> | <i lang="sa-Latn">gatyākṣepe</i> |
| <a id="dhatu-01-0116"></a>`01.0116` | <i lang="sa-Latn">√vaghi~\</i> | <i lang="sa-Latn">gatyākṣepe</i> |
| <a id="dhatu-01-0117"></a>`01.0117` | <i lang="sa-Latn">√maghi~\</i> | <i lang="sa-Latn">gatyākṣepe gatyārambhe kaitave ca</i> |
| <a id="dhatu-01-0118"></a>`01.0118` | <i lang="sa-Latn">√rāghṛ~\</i> | <i lang="sa-Latn">sāmarthye</i> |
| <a id="dhatu-01-0119"></a>`01.0119` | <i lang="sa-Latn">√lāghṛ~\</i> | <i lang="sa-Latn">sāmarthye</i> |
| <a id="dhatu-01-0120"></a>`01.0120` | <i lang="sa-Latn">√drāghṛ~\</i> | <i lang="sa-Latn">sāmarthye āyāme ca</i> |
| <a id="dhatu-01-0121"></a>`01.0121` | <i lang="sa-Latn">√dhrāghṛ~\</i> | <i lang="sa-Latn">sāmarthye</i> |
| <a id="dhatu-01-0122"></a>`01.0122` | <i lang="sa-Latn">√ślāghṛ~\</i> | <i lang="sa-Latn">katthane</i> |
| <a id="dhatu-01-0123"></a>`01.0123` | <i lang="sa-Latn">√phakka~</i> | <i lang="sa-Latn">nīcairgatau</i> |
| <a id="dhatu-01-0124"></a>`01.0124` | <i lang="sa-Latn">√taka~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0125"></a>`01.0125` | <i lang="sa-Latn">√taki~</i> | <i lang="sa-Latn">kṛcchrajīvane</i> |
| <a id="dhatu-01-0126"></a>`01.0126` | <i lang="sa-Latn">√bukka~</i> | <i lang="sa-Latn">bhaṣaṇe</i> |
| <a id="dhatu-01-0127"></a>`01.0127` | <i lang="sa-Latn">√śuka~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0128"></a>`01.0128` | <i lang="sa-Latn">√kakha~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0129"></a>`01.0129` | <i lang="sa-Latn">√okhṛ~</i> | <i lang="sa-Latn">śoṣaṇālamarthayoḥ</i> |
| <a id="dhatu-01-0130"></a>`01.0130` | <i lang="sa-Latn">√rākhṛ~</i> | <i lang="sa-Latn">śoṣaṇālamarthayoḥ</i> |
| <a id="dhatu-01-0131"></a>`01.0131` | <i lang="sa-Latn">√lākhṛ~</i> | <i lang="sa-Latn">śoṣaṇālamarthayoḥ</i> |
| <a id="dhatu-01-0132"></a>`01.0132` | <i lang="sa-Latn">√drākhṛ~</i> | <i lang="sa-Latn">śoṣaṇālamarthayoḥ</i> |
| <a id="dhatu-01-0133"></a>`01.0133` | <i lang="sa-Latn">√dhrākhṛ~</i> | <i lang="sa-Latn">śoṣaṇālamarthayoḥ</i> |
| <a id="dhatu-01-0134"></a>`01.0134` | <i lang="sa-Latn">√śākhṛ~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-01-0135"></a>`01.0135` | <i lang="sa-Latn">√ślākhṛ~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-01-0136"></a>`01.0136` | <i lang="sa-Latn">√ukha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0137"></a>`01.0137` | <i lang="sa-Latn">√ukhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0138"></a>`01.0138` | <i lang="sa-Latn">√vakha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0139"></a>`01.0139` | <i lang="sa-Latn">√vakhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0140"></a>`01.0140` | <i lang="sa-Latn">√makha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0141"></a>`01.0141` | <i lang="sa-Latn">√makhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0142"></a>`01.0142` | <i lang="sa-Latn">√ṇakha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0143"></a>`01.0143` | <i lang="sa-Latn">√ṇakhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0144"></a>`01.0144` | <i lang="sa-Latn">√rakha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0145"></a>`01.0145` | <i lang="sa-Latn">√rakhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0146"></a>`01.0146` | <i lang="sa-Latn">√lakha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0147"></a>`01.0147` | <i lang="sa-Latn">√lakhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0148"></a>`01.0148` | <i lang="sa-Latn">√ikha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0149"></a>`01.0149` | <i lang="sa-Latn">√ikhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0150"></a>`01.0150` | <i lang="sa-Latn">√jabha~</i> | <i lang="sa-Latn">gātravināme</i> |
| <a id="dhatu-01-0151"></a>`01.0151` | <i lang="sa-Latn">√īkhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0152"></a>`01.0152` | <i lang="sa-Latn">√valga~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0153"></a>`01.0153` | <i lang="sa-Latn">√ragi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0154"></a>`01.0154` | <i lang="sa-Latn">√lagi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0155"></a>`01.0155` | <i lang="sa-Latn">√agi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0156"></a>`01.0156` | <i lang="sa-Latn">√vagi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0157"></a>`01.0157` | <i lang="sa-Latn">√magi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0158"></a>`01.0158` | <i lang="sa-Latn">√tagi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0159"></a>`01.0159` | <i lang="sa-Latn">√tvagi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0160"></a>`01.0160` | <i lang="sa-Latn">√śvelṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0161"></a>`01.0161` | <i lang="sa-Latn">√śragi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0162"></a>`01.0162` | <i lang="sa-Latn">√ślagi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0163"></a>`01.0163` | <i lang="sa-Latn">√igi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0164"></a>`01.0164` | <i lang="sa-Latn">√rigi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0165"></a>`01.0165` | <i lang="sa-Latn">√ligi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0166"></a>`01.0166` | <i lang="sa-Latn">√kharkha~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0167"></a>`01.0167` | <i lang="sa-Latn">√kakkha</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0168"></a>`01.0168` | <i lang="sa-Latn">√rikha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0169"></a>`01.0169` | <i lang="sa-Latn">√gharba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0170"></a>`01.0170` | <i lang="sa-Latn">√narba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0171"></a>`01.0171` | <i lang="sa-Latn">√bharba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0172"></a>`01.0172` | <i lang="sa-Latn">√trakha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0173"></a>`01.0173` | <i lang="sa-Latn">√trikhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0174"></a>`01.0174` | <i lang="sa-Latn">√śikhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0175"></a>`01.0175` | <i lang="sa-Latn">√yugi~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-01-0176"></a>`01.0176` | <i lang="sa-Latn">√jugi~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-01-0177"></a>`01.0177` | <i lang="sa-Latn">√bugi~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-01-0178"></a>`01.0178` | <i lang="sa-Latn">√vugi~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-01-0179"></a>`01.0179` | <i lang="sa-Latn">√ghagha~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0180"></a>`01.0180` | <i lang="sa-Latn">√ghaggha~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0181"></a>`01.0181` | <i lang="sa-Latn">√varba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0182"></a>`01.0182` | <i lang="sa-Latn">√babhra~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0183"></a>`01.0183` | <i lang="sa-Latn">√maghi~</i> | <i lang="sa-Latn">maṇḍane</i> |
| <a id="dhatu-01-0184"></a>`01.0184` | <i lang="sa-Latn">√śighi~</i> | <i lang="sa-Latn">āghrāṇe</i> |
| <a id="dhatu-01-0185"></a>`01.0185` | <i lang="sa-Latn">√maja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0186"></a>`01.0186` | <i lang="sa-Latn">√varca~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0187"></a>`01.0187` | <i lang="sa-Latn">√ṣaca~\</i> | <i lang="sa-Latn">secane sevane ca</i> |
| <a id="dhatu-01-0188"></a>`01.0188` | <i lang="sa-Latn">√locṛ~\</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-01-0189"></a>`01.0189` | <i lang="sa-Latn">√śaca~\</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0190"></a>`01.0190` | <i lang="sa-Latn">√śvaca~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0191"></a>`01.0191` | <i lang="sa-Latn">√śvaci~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0192"></a>`01.0192` | <i lang="sa-Latn">√kaca~\</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0193"></a>`01.0193` | <i lang="sa-Latn">√kaci~\</i> | <i lang="sa-Latn">dīptibandhanayoḥ</i> |
| <a id="dhatu-01-0194"></a>`01.0194` | <i lang="sa-Latn">√kāci~\</i> | <i lang="sa-Latn">dīptibandhanayoḥ</i> |
| <a id="dhatu-01-0195"></a>`01.0195` | <i lang="sa-Latn">√maca~\</i> | <i lang="sa-Latn">kalkane kathane ca</i> |
| <a id="dhatu-01-0196"></a>`01.0196` | <i lang="sa-Latn">√muci~\</i> | <i lang="sa-Latn">kalkane kathane ca</i> |
| <a id="dhatu-01-0197"></a>`01.0197` | <i lang="sa-Latn">√maci~\</i> | <i lang="sa-Latn">dhāraṇocchrāyapūjaneṣu</i> |
| <a id="dhatu-01-0198"></a>`01.0198` | <i lang="sa-Latn">√paci~\</i> | <i lang="sa-Latn">vyaktīkaraṇe</i> |
| <a id="dhatu-01-0199"></a>`01.0199` | <i lang="sa-Latn">√ṣṭuca~\</i> | <i lang="sa-Latn">prasāde</i> |
| <a id="dhatu-01-0200"></a>`01.0200` | <i lang="sa-Latn">√ṛja~\</i> | <i lang="sa-Latn">gatisthānārjanopārjaneṣu</i> |
| <a id="dhatu-01-0201"></a>`01.0201` | <i lang="sa-Latn">√ṛji~\</i> | <i lang="sa-Latn">bharjane</i> |
| <a id="dhatu-01-0202"></a>`01.0202` | <i lang="sa-Latn">√bhṛjī~\</i> | <i lang="sa-Latn">bharjane</i> |
| <a id="dhatu-01-0203"></a>`01.0203` | <i lang="sa-Latn">√ejṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0204"></a>`01.0204` | <i lang="sa-Latn">√bhrejṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0205"></a>`01.0205` | <i lang="sa-Latn">√bhrājṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0206"></a>`01.0206` | <i lang="sa-Latn">√kāḍṛ~\</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0207"></a>`01.0207` | <i lang="sa-Latn">√īja~\</i> | <i lang="sa-Latn">gatikutsanayoḥ</i> |
| <a id="dhatu-01-0208"></a>`01.0208` | <i lang="sa-Latn">√pebṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0209"></a>`01.0209` | <i lang="sa-Latn">√plebṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0210"></a>`01.0210` | <i lang="sa-Latn">√śuca~</i> | <i lang="sa-Latn">śoke</i> |
| <a id="dhatu-01-0211"></a>`01.0211` | <i lang="sa-Latn">√kuca~</i> | <i lang="sa-Latn">śabde tāre</i> |
| <a id="dhatu-01-0212"></a>`01.0212` | <i lang="sa-Latn">√kunca~</i> | <i lang="sa-Latn">gatikauṭilyālpībhāvayoḥ</i> |
| <a id="dhatu-01-0213"></a>`01.0213` | <i lang="sa-Latn">√krunca~</i> | <i lang="sa-Latn">gatikauṭilyālpībhāvayoḥ</i> |
| <a id="dhatu-01-0214"></a>`01.0214` | <i lang="sa-Latn">√lunca~</i> | <i lang="sa-Latn">apanayane</i> |
| <a id="dhatu-01-0215"></a>`01.0215` | <i lang="sa-Latn">√ancu~</i> | <i lang="sa-Latn">gatipūjanayoḥ</i> |
| <a id="dhatu-01-0216"></a>`01.0216` | <i lang="sa-Latn">√vancu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0217"></a>`01.0217` | <i lang="sa-Latn">√cancu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0218"></a>`01.0218` | <i lang="sa-Latn">√tancu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0219"></a>`01.0219` | <i lang="sa-Latn">√tvancu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0220"></a>`01.0220` | <i lang="sa-Latn">√mruncu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0221"></a>`01.0221` | <i lang="sa-Latn">√mluncu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0222"></a>`01.0222` | <i lang="sa-Latn">√mrucu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0223"></a>`01.0223` | <i lang="sa-Latn">√mlucu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0224"></a>`01.0224` | <i lang="sa-Latn">√grucu~</i> | <i lang="sa-Latn">steyakaraṇe</i> |
| <a id="dhatu-01-0225"></a>`01.0225` | <i lang="sa-Latn">√glucu~</i> | <i lang="sa-Latn">steyakaraṇe</i> |
| <a id="dhatu-01-0226"></a>`01.0226` | <i lang="sa-Latn">√kuju~</i> | <i lang="sa-Latn">steyakaraṇe</i> |
| <a id="dhatu-01-0227"></a>`01.0227` | <i lang="sa-Latn">√khuju~</i> | <i lang="sa-Latn">steyakaraṇe</i> |
| <a id="dhatu-01-0228"></a>`01.0228` | <i lang="sa-Latn">√gluncu~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0229"></a>`01.0229` | <i lang="sa-Latn">√ṣasja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0230"></a>`01.0230` | <i lang="sa-Latn">√guja~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0231"></a>`01.0231` | <i lang="sa-Latn">√guji~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0232"></a>`01.0232` | <i lang="sa-Latn">√arca~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-01-0233"></a>`01.0233` | <i lang="sa-Latn">√mlecha~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0234"></a>`01.0234` | <i lang="sa-Latn">√lacha~</i> | <i lang="sa-Latn">lakṣaṇe</i> |
| <a id="dhatu-01-0235"></a>`01.0235` | <i lang="sa-Latn">√lāchi~</i> | <i lang="sa-Latn">lakṣaṇe</i> |
| <a id="dhatu-01-0236"></a>`01.0236` | <i lang="sa-Latn">√vāchi~</i> | <i lang="sa-Latn">icchāyām</i> |
| <a id="dhatu-01-0237"></a>`01.0237` | <i lang="sa-Latn">√āchi~</i> | <i lang="sa-Latn">āyāme</i> |
| <a id="dhatu-01-0238"></a>`01.0238` | <i lang="sa-Latn">√hrīcha~</i> | <i lang="sa-Latn">lajjāyām</i> |
| <a id="dhatu-01-0239"></a>`01.0239` | <i lang="sa-Latn">√hurchā~</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-01-0240"></a>`01.0240` | <i lang="sa-Latn">√murchā~</i> | <i lang="sa-Latn">mohasamucchrāyayoḥ</i> |
| <a id="dhatu-01-0241"></a>`01.0241` | <i lang="sa-Latn">√sphurchā~</i> | <i lang="sa-Latn">vistṛtau</i> |
| <a id="dhatu-01-0242"></a>`01.0242` | <i lang="sa-Latn">√yucha~</i> | <i lang="sa-Latn">pramāde</i> |
| <a id="dhatu-01-0243"></a>`01.0243` | <i lang="sa-Latn">√uchi~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-01-0244"></a>`01.0244` | <i lang="sa-Latn">√uchī~</i> | <i lang="sa-Latn">vivāse</i> |
| <a id="dhatu-01-0245"></a>`01.0245` | <i lang="sa-Latn">√dhraja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0246"></a>`01.0246` | <i lang="sa-Latn">√dhraji~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0247"></a>`01.0247` | <i lang="sa-Latn">√aṭi~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0248"></a>`01.0248` | <i lang="sa-Latn">√rebṛ~</i> | <i lang="sa-Latn">plavagatau</i> |
| <a id="dhatu-01-0249"></a>`01.0249` | <i lang="sa-Latn">√dhṛja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0250"></a>`01.0250` | <i lang="sa-Latn">√dhṛji~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0251"></a>`01.0251` | <i lang="sa-Latn">√dhvaja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0252"></a>`01.0252` | <i lang="sa-Latn">√dhvaji~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0253"></a>`01.0253` | <i lang="sa-Latn">√ṣalṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0254"></a>`01.0254` | <i lang="sa-Latn">√kūja~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0255"></a>`01.0255` | <i lang="sa-Latn">√bhṛṣu~</i> | <i lang="sa-Latn">saṅgharṣe</i> |
| <a id="dhatu-01-0256"></a>`01.0256` | <i lang="sa-Latn">√arja~</i> | <i lang="sa-Latn">arjane</i> |
| <a id="dhatu-01-0257"></a>`01.0257` | <i lang="sa-Latn">√ṣarja~</i> | <i lang="sa-Latn">arjane</i> |
| <a id="dhatu-01-0258"></a>`01.0258` | <i lang="sa-Latn">√garja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0259"></a>`01.0259` | <i lang="sa-Latn">√tarja~</i> | <i lang="sa-Latn">bhartsane</i> |
| <a id="dhatu-01-0260"></a>`01.0260` | <i lang="sa-Latn">√karja~</i> | <i lang="sa-Latn">vyathane</i> |
| <a id="dhatu-01-0261"></a>`01.0261` | <i lang="sa-Latn">√kharja~</i> | <i lang="sa-Latn">vyathane pūjane mārjane ca</i> |
| <a id="dhatu-01-0262"></a>`01.0262` | <i lang="sa-Latn">√aja~</i> | <i lang="sa-Latn">gatikṣepaṇayoḥ</i> |
| <a id="dhatu-01-0263"></a>`01.0263` | <i lang="sa-Latn">√teja~</i> | <i lang="sa-Latn">pālane</i> |
| <a id="dhatu-01-0264"></a>`01.0264` | <i lang="sa-Latn">√khaja~</i> | <i lang="sa-Latn">manthe</i> |
| <a id="dhatu-01-0265"></a>`01.0265` | <i lang="sa-Latn">√kava~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0266"></a>`01.0266` | <i lang="sa-Latn">√khaji~</i> | <i lang="sa-Latn">gativaikalye</i> |
| <a id="dhatu-01-0267"></a>`01.0267` | <i lang="sa-Latn">√ejṛ~</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-01-0268"></a>`01.0268` | <i lang="sa-Latn">√ṭuo~sphūrjā~</i> | <i lang="sa-Latn">vajranirghoṣe</i> |
| <a id="dhatu-01-0269"></a>`01.0269` | <i lang="sa-Latn">√kṣi\</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-01-0270"></a>`01.0270` | <i lang="sa-Latn">√kṣīja~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0271"></a>`01.0271` | <i lang="sa-Latn">√laja~</i> | <i lang="sa-Latn">bharjane</i> |
| <a id="dhatu-01-0272"></a>`01.0272` | <i lang="sa-Latn">√laji~</i> | <i lang="sa-Latn">bharjane</i> |
| <a id="dhatu-01-0273"></a>`01.0273` | <i lang="sa-Latn">√lāja~</i> | <i lang="sa-Latn">bharjane bhartsane ca</i> |
| <a id="dhatu-01-0274"></a>`01.0274` | <i lang="sa-Latn">√lāji~</i> | <i lang="sa-Latn">bharjane bhartsane ca</i> |
| <a id="dhatu-01-0275"></a>`01.0275` | <i lang="sa-Latn">√jaja~</i> | <i lang="sa-Latn">yuddhe</i> |
| <a id="dhatu-01-0276"></a>`01.0276` | <i lang="sa-Latn">√jaji~</i> | <i lang="sa-Latn">yuddhe</i> |
| <a id="dhatu-01-0277"></a>`01.0277` | <i lang="sa-Latn">√tuja~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0278"></a>`01.0278` | <i lang="sa-Latn">√tuji~</i> | <i lang="sa-Latn">pālane</i> |
| <a id="dhatu-01-0279"></a>`01.0279` | <i lang="sa-Latn">√gaja~</i> | <i lang="sa-Latn">śabde madane ca</i> |
| <a id="dhatu-01-0280"></a>`01.0280` | <i lang="sa-Latn">√gaji~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0281"></a>`01.0281` | <i lang="sa-Latn">√gṛja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0282"></a>`01.0282` | <i lang="sa-Latn">√gṛji~</i> | <i lang="sa-Latn">garjane</i> |
| <a id="dhatu-01-0283"></a>`01.0283` | <i lang="sa-Latn">√muja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0284"></a>`01.0284` | <i lang="sa-Latn">√muji~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0285"></a>`01.0285` | <i lang="sa-Latn">√vaja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0286"></a>`01.0286` | <i lang="sa-Latn">√vraja~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0287"></a>`01.0287` | <i lang="sa-Latn">√aṭṭa~\</i> | <i lang="sa-Latn">atikramahiṃsayoḥ</i> |
| <a id="dhatu-01-0288"></a>`01.0288` | <i lang="sa-Latn">√veṣṭa~\</i> | <i lang="sa-Latn">veṣṭane</i> |
| <a id="dhatu-01-0289"></a>`01.0289` | <i lang="sa-Latn">√ceṣṭa~\</i> | <i lang="sa-Latn">ceṣṭāyām</i> |
| <a id="dhatu-01-0290"></a>`01.0290` | <i lang="sa-Latn">√goṣṭa~\</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0291"></a>`01.0291` | <i lang="sa-Latn">√loṣṭa~\</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0292"></a>`01.0292` | <i lang="sa-Latn">√ghaṭṭa~\</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0293"></a>`01.0293` | <i lang="sa-Latn">√sphuṭa~\</i> | <i lang="sa-Latn">vikasane</i> |
| <a id="dhatu-01-0294"></a>`01.0294` | <i lang="sa-Latn">√aṭhi~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0295"></a>`01.0295` | <i lang="sa-Latn">√vaṭhi~\</i> | <i lang="sa-Latn">ekacaryāyām</i> |
| <a id="dhatu-01-0296"></a>`01.0296` | <i lang="sa-Latn">√maṭhi~\</i> | <i lang="sa-Latn">śoke</i> |
| <a id="dhatu-01-0297"></a>`01.0297` | <i lang="sa-Latn">√kaṭhi~\</i> | <i lang="sa-Latn">śoke</i> |
| <a id="dhatu-01-0298"></a>`01.0298` | <i lang="sa-Latn">√muṭhi~\</i> | <i lang="sa-Latn">pālane</i> |
| <a id="dhatu-01-0299"></a>`01.0299` | <i lang="sa-Latn">√heṭha~\</i> | <i lang="sa-Latn">vibādhāyām</i> |
| <a id="dhatu-01-0300"></a>`01.0300` | <i lang="sa-Latn">√eṭha~\</i> | <i lang="sa-Latn">vibādhāyām</i> |
| <a id="dhatu-01-0301"></a>`01.0301` | <i lang="sa-Latn">√hiḍi~\</i> | <i lang="sa-Latn">gatyanādarayoḥ</i> |
| <a id="dhatu-01-0302"></a>`01.0302` | <i lang="sa-Latn">√huḍi~\</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0303"></a>`01.0303` | <i lang="sa-Latn">√kuḍi~\</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0304"></a>`01.0304` | <i lang="sa-Latn">√vaḍi~\</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-01-0305"></a>`01.0305` | <i lang="sa-Latn">√maḍi~\</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-01-0306"></a>`01.0306` | <i lang="sa-Latn">√bhaḍi~\</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0307"></a>`01.0307` | <i lang="sa-Latn">√piḍi~\</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0308"></a>`01.0308` | <i lang="sa-Latn">√muḍi~\</i> | <i lang="sa-Latn">mārjane</i> |
| <a id="dhatu-01-0309"></a>`01.0309` | <i lang="sa-Latn">√tuḍi~\</i> | <i lang="sa-Latn">toḍane</i> |
| <a id="dhatu-01-0310"></a>`01.0310` | <i lang="sa-Latn">√huḍi~\</i> | <i lang="sa-Latn">varaṇe haraṇe ca</i> |
| <a id="dhatu-01-0311"></a>`01.0311` | <i lang="sa-Latn">√sphuḍi~\</i> | <i lang="sa-Latn">vikasane</i> |
| <a id="dhatu-01-0312"></a>`01.0312` | <i lang="sa-Latn">√caḍi~\</i> | <i lang="sa-Latn">kope</i> |
| <a id="dhatu-01-0313"></a>`01.0313` | <i lang="sa-Latn">√śaḍi~\</i> | <i lang="sa-Latn">rujāyāṃ saṅghāte ca</i> |
| <a id="dhatu-01-0314"></a>`01.0314` | <i lang="sa-Latn">√taḍi~\</i> | <i lang="sa-Latn">tāḍane</i> |
| <a id="dhatu-01-0315"></a>`01.0315` | <i lang="sa-Latn">√paḍi~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0316"></a>`01.0316` | <i lang="sa-Latn">√kaḍi~\</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-01-0317"></a>`01.0317` | <i lang="sa-Latn">√khaḍi~\</i> | <i lang="sa-Latn">manthe</i> |
| <a id="dhatu-01-0318"></a>`01.0318` | <i lang="sa-Latn">√heḍṛ~\</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0319"></a>`01.0319` | <i lang="sa-Latn">√hoḍṛ~\</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0320"></a>`01.0320` | <i lang="sa-Latn">√bāḍṛ~\</i> | <i lang="sa-Latn">āplāvye</i> |
| <a id="dhatu-01-0321"></a>`01.0321` | <i lang="sa-Latn">√vāḍṛ~\</i> | <i lang="sa-Latn">āplāvye</i> |
| <a id="dhatu-01-0322"></a>`01.0322` | <i lang="sa-Latn">√drāḍṛ~\</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0323"></a>`01.0323` | <i lang="sa-Latn">√dhrāḍṛ~\</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0324"></a>`01.0324` | <i lang="sa-Latn">√śāḍṛ~\</i> | <i lang="sa-Latn">ślāghāyām</i> |
| <a id="dhatu-01-0325"></a>`01.0325` | <i lang="sa-Latn">√śauṭṛ~</i> | <i lang="sa-Latn">garve</i> |
| <a id="dhatu-01-0326"></a>`01.0326` | <i lang="sa-Latn">√yauṭṛ~</i> | <i lang="sa-Latn">bandhe</i> |
| <a id="dhatu-01-0327"></a>`01.0327` | <i lang="sa-Latn">√meḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0328"></a>`01.0328` | <i lang="sa-Latn">√mreḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0329"></a>`01.0329` | <i lang="sa-Latn">√mleṭṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0330"></a>`01.0330` | <i lang="sa-Latn">√caṭe~</i> | <i lang="sa-Latn">varṣāvaraṇayoḥ</i> |
| <a id="dhatu-01-0331"></a>`01.0331` | <i lang="sa-Latn">√kaṭe~</i> | <i lang="sa-Latn">varṣāvaraṇayoḥ</i> |
| <a id="dhatu-01-0332"></a>`01.0332` | <i lang="sa-Latn">√aṭa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0333"></a>`01.0333` | <i lang="sa-Latn">√paṭa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0334"></a>`01.0334` | <i lang="sa-Latn">√raṭa~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0335"></a>`01.0335` | <i lang="sa-Latn">√laṭa~</i> | <i lang="sa-Latn">bālye</i> |
| <a id="dhatu-01-0336"></a>`01.0336` | <i lang="sa-Latn">√śaṭa~</i> | <i lang="sa-Latn">rujāviśaraṇagatyavasādaneṣu</i> |
| <a id="dhatu-01-0337"></a>`01.0337` | <i lang="sa-Latn">√vaṭa~</i> | <i lang="sa-Latn">veṣṭane</i> |
| <a id="dhatu-01-0338"></a>`01.0338` | <i lang="sa-Latn">√kiṭa~</i> | <i lang="sa-Latn">trāse</i> |
| <a id="dhatu-01-0339"></a>`01.0339` | <i lang="sa-Latn">√khiṭa~</i> | <i lang="sa-Latn">trāse</i> |
| <a id="dhatu-01-0340"></a>`01.0340` | <i lang="sa-Latn">√śiṭa~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0341"></a>`01.0341` | <i lang="sa-Latn">√ṣiṭa~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0342"></a>`01.0342` | <i lang="sa-Latn">√jaṭa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0343"></a>`01.0343` | <i lang="sa-Latn">√jhaṭa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0344"></a>`01.0344` | <i lang="sa-Latn">√bhaṭa~</i> | <i lang="sa-Latn">bhṛtau</i> |
| <a id="dhatu-01-0345"></a>`01.0345` | <i lang="sa-Latn">√taṭa~</i> | <i lang="sa-Latn">ucchrāye</i> |
| <a id="dhatu-01-0346"></a>`01.0346` | <i lang="sa-Latn">√khaṭa~</i> | <i lang="sa-Latn">kāṅkṣāyām</i> |
| <a id="dhatu-01-0347"></a>`01.0347` | <i lang="sa-Latn">√ṇaṭa~</i> | <i lang="sa-Latn">nṛttau</i> |
| <a id="dhatu-01-0348"></a>`01.0348` | <i lang="sa-Latn">√piṭa~</i> | <i lang="sa-Latn">śabdasaṅghātayoḥ</i> |
| <a id="dhatu-01-0349"></a>`01.0349` | <i lang="sa-Latn">√haṭa~</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0350"></a>`01.0350` | <i lang="sa-Latn">√ṣaṭa~</i> | <i lang="sa-Latn">avayave</i> |
| <a id="dhatu-01-0351"></a>`01.0351` | <i lang="sa-Latn">√luṭa~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-01-0352"></a>`01.0352` | <i lang="sa-Latn">√luḍa~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-01-0353"></a>`01.0353` | <i lang="sa-Latn">√ciṭa~</i> | <i lang="sa-Latn">parapraiṣye</i> |
| <a id="dhatu-01-0354"></a>`01.0354` | <i lang="sa-Latn">√viṭa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0355"></a>`01.0355` | <i lang="sa-Latn">√biṭa~</i> | <i lang="sa-Latn">ākrośe</i> |
| <a id="dhatu-01-0356"></a>`01.0356` | <i lang="sa-Latn">√hiṭa~</i> | <i lang="sa-Latn">ākrośe</i> |
| <a id="dhatu-01-0357"></a>`01.0357` | <i lang="sa-Latn">√iṭa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0358"></a>`01.0358` | <i lang="sa-Latn">√kiṭa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0359"></a>`01.0359` | <i lang="sa-Latn">√kaṭī~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0360"></a>`01.0360` | <i lang="sa-Latn">√cuṭi~</i> | <i lang="sa-Latn">alpībhāve</i> |
| <a id="dhatu-01-0361"></a>`01.0361` | <i lang="sa-Latn">√maḍi~</i> | <i lang="sa-Latn">bhūṣāyām</i> |
| <a id="dhatu-01-0362"></a>`01.0362` | <i lang="sa-Latn">√kuḍi~</i> | <i lang="sa-Latn">vaikalye</i> |
| <a id="dhatu-01-0363"></a>`01.0363` | <i lang="sa-Latn">√kuṭhi~</i> | <i lang="sa-Latn">vaikalye</i> |
| <a id="dhatu-01-0364"></a>`01.0364` | <i lang="sa-Latn">√muḍa~</i> | <i lang="sa-Latn">mardane</i> |
| <a id="dhatu-01-0365"></a>`01.0365` | <i lang="sa-Latn">√pruḍa~</i> | <i lang="sa-Latn">mardane vimardane</i> |
| <a id="dhatu-01-0366"></a>`01.0366` | <i lang="sa-Latn">√muṭa~</i> | <i lang="sa-Latn">mardane</i> |
| <a id="dhatu-01-0367"></a>`01.0367` | <i lang="sa-Latn">√puḍa~</i> | <i lang="sa-Latn">mardane</i> |
| <a id="dhatu-01-0368"></a>`01.0368` | <i lang="sa-Latn">√cuḍi~</i> | <i lang="sa-Latn">alpībhāve</i> |
| <a id="dhatu-01-0369"></a>`01.0369` | <i lang="sa-Latn">√muḍi~</i> | <i lang="sa-Latn">khaṇḍane</i> |
| <a id="dhatu-01-0370"></a>`01.0370` | <i lang="sa-Latn">√puḍi~</i> | <i lang="sa-Latn">khaṇḍane</i> |
| <a id="dhatu-01-0371"></a>`01.0371` | <i lang="sa-Latn">√ruṭi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0372"></a>`01.0372` | <i lang="sa-Latn">√luṭi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0373"></a>`01.0373` | <i lang="sa-Latn">√ruṭhi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0374"></a>`01.0374` | <i lang="sa-Latn">√luṭhi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0375"></a>`01.0375` | <i lang="sa-Latn">√ruḍi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0376"></a>`01.0376` | <i lang="sa-Latn">√luḍi~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0377"></a>`01.0377` | <i lang="sa-Latn">√vaṭi~</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-01-0378"></a>`01.0378` | <i lang="sa-Latn">√sphaṭi~</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0379"></a>`01.0379` | <i lang="sa-Latn">√sphuṭi~r</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0380"></a>`01.0380` | <i lang="sa-Latn">√sphuṭi~</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0381"></a>`01.0381` | <i lang="sa-Latn">√paṭha~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0382"></a>`01.0382` | <i lang="sa-Latn">√vaṭha~</i> | <i lang="sa-Latn">sthaulye</i> |
| <a id="dhatu-01-0383"></a>`01.0383` | <i lang="sa-Latn">√hauḍṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0384"></a>`01.0384` | <i lang="sa-Latn">√maṭha~</i> | <i lang="sa-Latn">madanivāsayoḥ</i> |
| <a id="dhatu-01-0385"></a>`01.0385` | <i lang="sa-Latn">√kaṭha~</i> | <i lang="sa-Latn">kṛcchrajīvane</i> |
| <a id="dhatu-01-0386"></a>`01.0386` | <i lang="sa-Latn">√raṭha~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0387"></a>`01.0387` | <i lang="sa-Latn">√raṭa~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0388"></a>`01.0388` | <i lang="sa-Latn">√haṭha~</i> | <i lang="sa-Latn">plutiśaṭhatvayoḥ balātkāre ca</i> |
| <a id="dhatu-01-0389"></a>`01.0389` | <i lang="sa-Latn">√ruṭha~</i> | <i lang="sa-Latn">upaghāte</i> |
| <a id="dhatu-01-0390"></a>`01.0390` | <i lang="sa-Latn">√luṭha~</i> | <i lang="sa-Latn">upaghāte</i> |
| <a id="dhatu-01-0391"></a>`01.0391` | <i lang="sa-Latn">√ūṭha~</i> | <i lang="sa-Latn">upaghāte</i> |
| <a id="dhatu-01-0392"></a>`01.0392` | <i lang="sa-Latn">√uṭha~</i> | <i lang="sa-Latn">upaghāte</i> |
| <a id="dhatu-01-0393"></a>`01.0393` | <i lang="sa-Latn">√piṭha~</i> | <i lang="sa-Latn">hiṃsāsaṅkleśanayoḥ</i> |
| <a id="dhatu-01-0394"></a>`01.0394` | <i lang="sa-Latn">√śaṭha~</i> | <i lang="sa-Latn">kaitave hiṃsāsaṅkleśanayoḥ dyūte spardhāyāṃ ca</i> |
| <a id="dhatu-01-0395"></a>`01.0395` | <i lang="sa-Latn">√śuṭha~</i> | <i lang="sa-Latn">pratighāte gatipratighāte ca</i> |
| <a id="dhatu-01-0396"></a>`01.0396` | <i lang="sa-Latn">√śūṭha~</i> | <i lang="sa-Latn">gatipratighāte</i> |
| <a id="dhatu-01-0397"></a>`01.0397` | <i lang="sa-Latn">√kuṭhi~</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-01-0398"></a>`01.0398` | <i lang="sa-Latn">√luṭhi~</i> | <i lang="sa-Latn">ālasye pratighāte ca</i> |
| <a id="dhatu-01-0399"></a>`01.0399` | <i lang="sa-Latn">√śuṭhi~</i> | <i lang="sa-Latn">śoṣaṇe</i> |
| <a id="dhatu-01-0400"></a>`01.0400` | <i lang="sa-Latn">√ruṭhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0401"></a>`01.0401` | <i lang="sa-Latn">√luṭhi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0402"></a>`01.0402` | <i lang="sa-Latn">√cuḍḍa~</i> | <i lang="sa-Latn">bhāvakaraṇe</i> |
| <a id="dhatu-01-0403"></a>`01.0403` | <i lang="sa-Latn">√aḍḍa~</i> | <i lang="sa-Latn">abhiyoge</i> |
| <a id="dhatu-01-0404"></a>`01.0404` | <i lang="sa-Latn">√kaḍḍa~</i> | <i lang="sa-Latn">kārkaśye</i> |
| <a id="dhatu-01-0405"></a>`01.0405` | <i lang="sa-Latn">√krīḍṛ~</i> | <i lang="sa-Latn">vihāre</i> |
| <a id="dhatu-01-0406"></a>`01.0406` | <i lang="sa-Latn">√tuḍṛ~</i> | <i lang="sa-Latn">toḍane</i> |
| <a id="dhatu-01-0407"></a>`01.0407` | <i lang="sa-Latn">√tūḍṛ~</i> | <i lang="sa-Latn">toḍane</i> |
| <a id="dhatu-01-0408"></a>`01.0408` | <i lang="sa-Latn">√huḍṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0409"></a>`01.0409` | <i lang="sa-Latn">√hūḍṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0410"></a>`01.0410` | <i lang="sa-Latn">√hoḍṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0411"></a>`01.0411` | <i lang="sa-Latn">√rauḍṛ~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-01-0412"></a>`01.0412` | <i lang="sa-Latn">√roḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0413"></a>`01.0413` | <i lang="sa-Latn">√loḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0414"></a>`01.0414` | <i lang="sa-Latn">√aḍa~</i> | <i lang="sa-Latn">udyame</i> |
| <a id="dhatu-01-0415"></a>`01.0415` | <i lang="sa-Latn">√laḍa~</i> | <i lang="sa-Latn">vilāse</i> |
| <a id="dhatu-01-0416"></a>`01.0416` | <i lang="sa-Latn">√lala~</i> | <i lang="sa-Latn">vilāse</i> |
| <a id="dhatu-01-0417"></a>`01.0417` | <i lang="sa-Latn">√kaḍa~</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-01-0418"></a>`01.0418` | <i lang="sa-Latn">√kaḍi~</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-01-0419"></a>`01.0419` | <i lang="sa-Latn">√gaḍi~</i> | <i lang="sa-Latn">vadanaikadeśe</i> |
| <a id="dhatu-01-0420"></a>`01.0420` | <i lang="sa-Latn">√ti\pṛ~\</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-01-0421"></a>`01.0421` | <i lang="sa-Latn">√tepṛ~\</i> | <i lang="sa-Latn">kṣaraṇe kampane ca</i> |
| <a id="dhatu-01-0422"></a>`01.0422` | <i lang="sa-Latn">√ṣṭipṛ~\</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-01-0423"></a>`01.0423` | <i lang="sa-Latn">√ṣṭepṛ~\</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-01-0424"></a>`01.0424` | <i lang="sa-Latn">√glepṛ~\</i> | <i lang="sa-Latn">dainye</i> |
| <a id="dhatu-01-0425"></a>`01.0425` | <i lang="sa-Latn">√ṭuvepṛ~\</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-01-0426"></a>`01.0426` | <i lang="sa-Latn">√kepṛ~\</i> | <i lang="sa-Latn">kampane gatau ca</i> |
| <a id="dhatu-01-0427"></a>`01.0427` | <i lang="sa-Latn">√gepṛ~\</i> | <i lang="sa-Latn">kampane gatau ca</i> |
| <a id="dhatu-01-0428"></a>`01.0428` | <i lang="sa-Latn">√glepṛ~\</i> | <i lang="sa-Latn">kampane gatau ca</i> |
| <a id="dhatu-01-0429"></a>`01.0429` | <i lang="sa-Latn">√mepṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0430"></a>`01.0430` | <i lang="sa-Latn">√repṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0431"></a>`01.0431` | <i lang="sa-Latn">√lepṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0432"></a>`01.0432` | <i lang="sa-Latn">√hepṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0433"></a>`01.0433` | <i lang="sa-Latn">√dhepṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0434"></a>`01.0434` | <i lang="sa-Latn">√trapū~\ṣ</i> | <i lang="sa-Latn">lajjāyām</i> |
| <a id="dhatu-01-0435"></a>`01.0435` | <i lang="sa-Latn">√kapi~\</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0436"></a>`01.0436` | <i lang="sa-Latn">√rabi~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0437"></a>`01.0437` | <i lang="sa-Latn">√labi~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0438"></a>`01.0438` | <i lang="sa-Latn">√abi~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0439"></a>`01.0439` | <i lang="sa-Latn">√labi~\</i> | <i lang="sa-Latn">avasraṃsane śabde ca</i> |
| <a id="dhatu-01-0440"></a>`01.0440` | <i lang="sa-Latn">√kabṛ~\</i> | <i lang="sa-Latn">varṇe</i> |
| <a id="dhatu-01-0441"></a>`01.0441` | <i lang="sa-Latn">√klībṛ~\</i> | <i lang="sa-Latn">adhārṣṭye</i> |
| <a id="dhatu-01-0442"></a>`01.0442` | <i lang="sa-Latn">√kṣībṛ~\</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-01-0443"></a>`01.0443` | <i lang="sa-Latn">√kṣīvṛ~\</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-01-0444"></a>`01.0444` | <i lang="sa-Latn">√śībhṛ~\</i> | <i lang="sa-Latn">katthane</i> |
| <a id="dhatu-01-0445"></a>`01.0445` | <i lang="sa-Latn">√lauḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0446"></a>`01.0446` | <i lang="sa-Latn">√cībhṛ~\</i> | <i lang="sa-Latn">katthane</i> |
| <a id="dhatu-01-0447"></a>`01.0447` | <i lang="sa-Latn">√rebhṛ~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0448"></a>`01.0448` | <i lang="sa-Latn">√abhi~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0449"></a>`01.0449` | <i lang="sa-Latn">√rabhi~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0450"></a>`01.0450` | <i lang="sa-Latn">√ṣidhu~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-01-0451"></a>`01.0451` | <i lang="sa-Latn">√ṣṭabhi~\</i> | <i lang="sa-Latn">pratibandhe</i> |
| <a id="dhatu-01-0452"></a>`01.0452` | <i lang="sa-Latn">√skabhi~\</i> | <i lang="sa-Latn">pratibandhe</i> |
| <a id="dhatu-01-0453"></a>`01.0453` | <i lang="sa-Latn">√jabhī~\</i> | <i lang="sa-Latn">gātravināme</i> |
| <a id="dhatu-01-0454"></a>`01.0454` | <i lang="sa-Latn">√jṛbhi~\</i> | <i lang="sa-Latn">gātravināme</i> |
| <a id="dhatu-01-0455"></a>`01.0455` | <i lang="sa-Latn">√śalbha~\</i> | <i lang="sa-Latn">katthane</i> |
| <a id="dhatu-01-0456"></a>`01.0456` | <i lang="sa-Latn">√valbha~\</i> | <i lang="sa-Latn">bhojane</i> |
| <a id="dhatu-01-0457"></a>`01.0457` | <i lang="sa-Latn">√galbha~\</i> | <i lang="sa-Latn">dhārṣṭye</i> |
| <a id="dhatu-01-0458"></a>`01.0458` | <i lang="sa-Latn">√śranbhu~\</i> | <i lang="sa-Latn">pramāde</i> |
| <a id="dhatu-01-0459"></a>`01.0459` | <i lang="sa-Latn">√sranbhu~\</i> | <i lang="sa-Latn">pramāde</i> |
| <a id="dhatu-01-0460"></a>`01.0460` | <i lang="sa-Latn">√ṣṭubhu~\</i> | <i lang="sa-Latn">stambhe</i> |
| <a id="dhatu-01-0461"></a>`01.0461` | <i lang="sa-Latn">√gupū~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-01-0462"></a>`01.0462` | <i lang="sa-Latn">√dhūpa~</i> | <i lang="sa-Latn">santāpe</i> |
| <a id="dhatu-01-0463"></a>`01.0463` | <i lang="sa-Latn">√japa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci mānase ca</i> |
| <a id="dhatu-01-0464"></a>`01.0464` | <i lang="sa-Latn">√jalpa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0465"></a>`01.0465` | <i lang="sa-Latn">√capa~</i> | <i lang="sa-Latn">sāntvane</i> |
| <a id="dhatu-01-0466"></a>`01.0466` | <i lang="sa-Latn">√ṣapa~</i> | <i lang="sa-Latn">samavāye</i> |
| <a id="dhatu-01-0467"></a>`01.0467` | <i lang="sa-Latn">√rapa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0468"></a>`01.0468` | <i lang="sa-Latn">√lapa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0469"></a>`01.0469` | <i lang="sa-Latn">√cupa~</i> | <i lang="sa-Latn">mandāyāṃ gatau</i> |
| <a id="dhatu-01-0470"></a>`01.0470` | <i lang="sa-Latn">√tupa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0471"></a>`01.0471` | <i lang="sa-Latn">√tunpa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0472"></a>`01.0472` | <i lang="sa-Latn">√trupa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0473"></a>`01.0473` | <i lang="sa-Latn">√trunpa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0474"></a>`01.0474` | <i lang="sa-Latn">√tupha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0475"></a>`01.0475` | <i lang="sa-Latn">√tunpha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0476"></a>`01.0476` | <i lang="sa-Latn">√trupha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0477"></a>`01.0477` | <i lang="sa-Latn">√trunpha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0478"></a>`01.0478` | <i lang="sa-Latn">√parpa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0479"></a>`01.0479` | <i lang="sa-Latn">√rapha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0480"></a>`01.0480` | <i lang="sa-Latn">√raphi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0481"></a>`01.0481` | <i lang="sa-Latn">√arba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0482"></a>`01.0482` | <i lang="sa-Latn">√parba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0483"></a>`01.0483` | <i lang="sa-Latn">√larba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0484"></a>`01.0484` | <i lang="sa-Latn">√barba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0485"></a>`01.0485` | <i lang="sa-Latn">√marba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0486"></a>`01.0486` | <i lang="sa-Latn">√karba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0487"></a>`01.0487` | <i lang="sa-Latn">√kharba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0488"></a>`01.0488` | <i lang="sa-Latn">√garba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0489"></a>`01.0489` | <i lang="sa-Latn">√śarba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0490"></a>`01.0490` | <i lang="sa-Latn">√ṣarba~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0491"></a>`01.0491` | <i lang="sa-Latn">√carba~</i> | <i lang="sa-Latn">gatau ardane ca</i> |
| <a id="dhatu-01-0492"></a>`01.0492` | <i lang="sa-Latn">√kubi~</i> | <i lang="sa-Latn">chādane ācchādane ca</i> |
| <a id="dhatu-01-0493"></a>`01.0493` | <i lang="sa-Latn">√lubi~</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-01-0494"></a>`01.0494` | <i lang="sa-Latn">√tubi~</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-01-0495"></a>`01.0495` | <i lang="sa-Latn">√cubi~</i> | <i lang="sa-Latn">vaktrasaṃyoge</i> |
| <a id="dhatu-01-0496"></a>`01.0496` | <i lang="sa-Latn">√ṣṛbhu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0497"></a>`01.0497` | <i lang="sa-Latn">√ṣṛnbhu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0498"></a>`01.0498` | <i lang="sa-Latn">√ṣibhu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0499"></a>`01.0499` | <i lang="sa-Latn">√ṣinbhu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0500"></a>`01.0500` | <i lang="sa-Latn">√śubha~</i> | <i lang="sa-Latn">bhāṣaṇe bhāsane hiṃsāyāṃ ca</i> |
| <a id="dhatu-01-0501"></a>`01.0501` | <i lang="sa-Latn">√śunbha~</i> | <i lang="sa-Latn">bhāṣaṇe bhāsane hiṃsāyāṃ dīptau ca</i> |
| <a id="dhatu-01-0502"></a>`01.0502` | <i lang="sa-Latn">√ghiṇi~\</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-01-0503"></a>`01.0503` | <i lang="sa-Latn">√ghuṇi~\</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-01-0504"></a>`01.0504` | <i lang="sa-Latn">√ghṛṇi~\</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-01-0505"></a>`01.0505` | <i lang="sa-Latn">√ghuṇa~\</i> | <i lang="sa-Latn">bhramaṇe</i> |
| <a id="dhatu-01-0506"></a>`01.0506` | <i lang="sa-Latn">√ghurṇa~\</i> | <i lang="sa-Latn">bhramaṇe</i> |
| <a id="dhatu-01-0507"></a>`01.0507` | <i lang="sa-Latn">√paṇa~\</i> | <i lang="sa-Latn">vyavahāre stutau ca</i> |
| <a id="dhatu-01-0508"></a>`01.0508` | <i lang="sa-Latn">√pana~\</i> | <i lang="sa-Latn">vyavahāre stutau ca</i> |
| <a id="dhatu-01-0509"></a>`01.0509` | <i lang="sa-Latn">√bhāma~\</i> | <i lang="sa-Latn">krodhe</i> |
| <a id="dhatu-01-0510"></a>`01.0510` | <i lang="sa-Latn">√kṣamū~\ṣ</i> | <i lang="sa-Latn">sahane</i> |
| <a id="dhatu-01-0511"></a>`01.0511` | <i lang="sa-Latn">√kamu~\</i> | <i lang="sa-Latn">kāntau</i> |
| <a id="dhatu-01-0512"></a>`01.0512` | <i lang="sa-Latn">√aṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0513"></a>`01.0513` | <i lang="sa-Latn">√raṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0514"></a>`01.0514` | <i lang="sa-Latn">√vaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0515"></a>`01.0515` | <i lang="sa-Latn">√bhaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0516"></a>`01.0516` | <i lang="sa-Latn">√maṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0517"></a>`01.0517` | <i lang="sa-Latn">√kaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0518"></a>`01.0518` | <i lang="sa-Latn">√kvaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0519"></a>`01.0519` | <i lang="sa-Latn">√vraṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0520"></a>`01.0520` | <i lang="sa-Latn">√bhraṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0521"></a>`01.0521` | <i lang="sa-Latn">√dhvaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0522"></a>`01.0522` | <i lang="sa-Latn">√dhaṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0523"></a>`01.0523` | <i lang="sa-Latn">√oṇṛ~</i> | <i lang="sa-Latn">apanayane</i> |
| <a id="dhatu-01-0524"></a>`01.0524` | <i lang="sa-Latn">√śoṇṛ~</i> | <i lang="sa-Latn">varṇagatyoḥ</i> |
| <a id="dhatu-01-0525"></a>`01.0525` | <i lang="sa-Latn">√śroṇṛ~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0526"></a>`01.0526` | <i lang="sa-Latn">√śloṇṛ~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0527"></a>`01.0527` | <i lang="sa-Latn">√paiṇṛ~</i> | <i lang="sa-Latn">gatipreraṇaśleṣaṇeṣu</i> |
| <a id="dhatu-01-0528"></a>`01.0528` | <i lang="sa-Latn">√praiṇṛ~</i> | <i lang="sa-Latn">gatipreraṇaśleṣaṇeṣu</i> |
| <a id="dhatu-01-0529"></a>`01.0529` | <i lang="sa-Latn">√dhraṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0530"></a>`01.0530` | <i lang="sa-Latn">√baṇa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0531"></a>`01.0531` | <i lang="sa-Latn">√kanī~</i> | <i lang="sa-Latn">dīptikāntigatiṣu</i> |
| <a id="dhatu-01-0532"></a>`01.0532` | <i lang="sa-Latn">√ṣṭana~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0533"></a>`01.0533` | <i lang="sa-Latn">√vana~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0534"></a>`01.0534` | <i lang="sa-Latn">√vana~</i> | <i lang="sa-Latn">sambhaktau</i> |
| <a id="dhatu-01-0535"></a>`01.0535` | <i lang="sa-Latn">√ṣaṇa~</i> | <i lang="sa-Latn">sambhaktau</i> |
| <a id="dhatu-01-0536"></a>`01.0536` | <i lang="sa-Latn">√ama~</i> | <i lang="sa-Latn">gatau śabde sambhaktau ca</i> |
| <a id="dhatu-01-0537"></a>`01.0537` | <i lang="sa-Latn">√drama~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0538"></a>`01.0538` | <i lang="sa-Latn">√hamma~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0539"></a>`01.0539` | <i lang="sa-Latn">√mīmṛ~</i> | <i lang="sa-Latn">gatau śabde ca</i> |
| <a id="dhatu-01-0540"></a>`01.0540` | <i lang="sa-Latn">√camu~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0541"></a>`01.0541` | <i lang="sa-Latn">√chamu~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0542"></a>`01.0542` | <i lang="sa-Latn">√jamu~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0543"></a>`01.0543` | <i lang="sa-Latn">√jhamu~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0544"></a>`01.0544` | <i lang="sa-Latn">√jimu~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0545"></a>`01.0545` | <i lang="sa-Latn">√kramu~</i> | <i lang="sa-Latn">pādavikṣepe</i> |
| <a id="dhatu-01-0546"></a>`01.0546` | <i lang="sa-Latn">√aya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0547"></a>`01.0547` | <i lang="sa-Latn">√vaya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0548"></a>`01.0548` | <i lang="sa-Latn">√paya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0549"></a>`01.0549` | <i lang="sa-Latn">√maya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0550"></a>`01.0550` | <i lang="sa-Latn">√caya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0551"></a>`01.0551` | <i lang="sa-Latn">√taya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0552"></a>`01.0552` | <i lang="sa-Latn">√ṇaya~\</i> | <i lang="sa-Latn">gatau rakṣaṇe ca</i> |
| <a id="dhatu-01-0553"></a>`01.0553` | <i lang="sa-Latn">√daya~\</i> | <i lang="sa-Latn">dānagatirakṣaṇahiṃsā'dāneṣu</i> |
| <a id="dhatu-01-0554"></a>`01.0554` | <i lang="sa-Latn">√raya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0555"></a>`01.0555` | <i lang="sa-Latn">√yaya~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0556"></a>`01.0556` | <i lang="sa-Latn">√ūyī~\</i> | <i lang="sa-Latn">tantusantāne</i> |
| <a id="dhatu-01-0557"></a>`01.0557` | <i lang="sa-Latn">√pūyī~\</i> | <i lang="sa-Latn">viśaraṇe durgandhe ca</i> |
| <a id="dhatu-01-0558"></a>`01.0558` | <i lang="sa-Latn">√knūyī~\</i> | <i lang="sa-Latn">śabde undane ca</i> |
| <a id="dhatu-01-0559"></a>`01.0559` | <i lang="sa-Latn">√kṣmāyī~\</i> | <i lang="sa-Latn">vidhūnane</i> |
| <a id="dhatu-01-0560"></a>`01.0560` | <i lang="sa-Latn">√sphāyī~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0561"></a>`01.0561` | <i lang="sa-Latn">√o~pyāyī~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0562"></a>`01.0562` | <i lang="sa-Latn">√tāyṛ~\</i> | <i lang="sa-Latn">santānapālanayoḥ</i> |
| <a id="dhatu-01-0563"></a>`01.0563` | <i lang="sa-Latn">√śala~\</i> | <i lang="sa-Latn">calanasaṃvaraṇayoḥ</i> |
| <a id="dhatu-01-0564"></a>`01.0564` | <i lang="sa-Latn">√vala~\</i> | <i lang="sa-Latn">saṃvaraṇe sañcaraṇe ca</i> |
| <a id="dhatu-01-0565"></a>`01.0565` | <i lang="sa-Latn">√valla~\</i> | <i lang="sa-Latn">saṃvaraṇe sañcaraṇe ca</i> |
| <a id="dhatu-01-0566"></a>`01.0566` | <i lang="sa-Latn">√mala~\</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-01-0567"></a>`01.0567` | <i lang="sa-Latn">√malla~\</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-01-0568"></a>`01.0568` | <i lang="sa-Latn">√bhala~\</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsādāneṣu</i> |
| <a id="dhatu-01-0569"></a>`01.0569` | <i lang="sa-Latn">√bhalla~\</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsādāneṣu</i> |
| <a id="dhatu-01-0570"></a>`01.0570` | <i lang="sa-Latn">√kala~\</i> | <i lang="sa-Latn">śabdasaṅkhyānayoḥ</i> |
| <a id="dhatu-01-0571"></a>`01.0571` | <i lang="sa-Latn">√kalla~\</i> | <i lang="sa-Latn">avyakte śabde aśabde ca</i> |
| <a id="dhatu-01-0572"></a>`01.0572` | <i lang="sa-Latn">√tevṛ~\</i> | <i lang="sa-Latn">devane</i> |
| <a id="dhatu-01-0573"></a>`01.0573` | <i lang="sa-Latn">√devṛ~\</i> | <i lang="sa-Latn">devane</i> |
| <a id="dhatu-01-0574"></a>`01.0574` | <i lang="sa-Latn">√ṣevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0575"></a>`01.0575` | <i lang="sa-Latn">√gevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0576"></a>`01.0576` | <i lang="sa-Latn">√glevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0577"></a>`01.0577` | <i lang="sa-Latn">√pevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0578"></a>`01.0578` | <i lang="sa-Latn">√mevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0579"></a>`01.0579` | <i lang="sa-Latn">√mlevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0580"></a>`01.0580` | <i lang="sa-Latn">√śevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0581"></a>`01.0581` | <i lang="sa-Latn">√khevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0582"></a>`01.0582` | <i lang="sa-Latn">√plevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0583"></a>`01.0583` | <i lang="sa-Latn">√kevṛ~\</i> | <i lang="sa-Latn">sevane</i> |
| <a id="dhatu-01-0584"></a>`01.0584` | <i lang="sa-Latn">√revṛ~\</i> | <i lang="sa-Latn">plavagatau</i> |
| <a id="dhatu-01-0585"></a>`01.0585` | <i lang="sa-Latn">√mavya~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0586"></a>`01.0586` | <i lang="sa-Latn">√sūrkṣya~</i> | <i lang="sa-Latn">īrṣyāyām</i> |
| <a id="dhatu-01-0587"></a>`01.0587` | <i lang="sa-Latn">√īrkṣya~</i> | <i lang="sa-Latn">īrṣyāyām</i> |
| <a id="dhatu-01-0588"></a>`01.0588` | <i lang="sa-Latn">√īrṣya~</i> | <i lang="sa-Latn">īrṣyāyām</i> |
| <a id="dhatu-01-0589"></a>`01.0589` | <i lang="sa-Latn">√haya~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0590"></a>`01.0590` | <i lang="sa-Latn">√śucya~</i> | <i lang="sa-Latn">abhiṣave</i> |
| <a id="dhatu-01-0591"></a>`01.0591` | <i lang="sa-Latn">√cucya~</i> | <i lang="sa-Latn">abhiṣave</i> |
| <a id="dhatu-01-0592"></a>`01.0592` | <i lang="sa-Latn">√harya~</i> | <i lang="sa-Latn">gatikāntyoḥ</i> |
| <a id="dhatu-01-0593"></a>`01.0593` | <i lang="sa-Latn">√ala~</i> | <i lang="sa-Latn">bhūṣaṇaparyāptivāraṇeṣu</i> |
| <a id="dhatu-01-0594"></a>`01.0594` | <i lang="sa-Latn">√ñiphalā~</i> | <i lang="sa-Latn">viśaraṇe</i> |
| <a id="dhatu-01-0595"></a>`01.0595` | <i lang="sa-Latn">√mīla~</i> | <i lang="sa-Latn">nimeṣaṇe</i> |
| <a id="dhatu-01-0596"></a>`01.0596` | <i lang="sa-Latn">√śmīla~</i> | <i lang="sa-Latn">nimeṣaṇe</i> |
| <a id="dhatu-01-0597"></a>`01.0597` | <i lang="sa-Latn">√smīla~</i> | <i lang="sa-Latn">nimeṣaṇe</i> |
| <a id="dhatu-01-0598"></a>`01.0598` | <i lang="sa-Latn">√kṣmīla~</i> | <i lang="sa-Latn">nimeṣaṇe</i> |
| <a id="dhatu-01-0599"></a>`01.0599` | <i lang="sa-Latn">√pīla~</i> | <i lang="sa-Latn">pratiṣṭambhe</i> |
| <a id="dhatu-01-0600"></a>`01.0600` | <i lang="sa-Latn">√ṇīla~</i> | <i lang="sa-Latn">varṇe</i> |
| <a id="dhatu-01-0601"></a>`01.0601` | <i lang="sa-Latn">√śīla~</i> | <i lang="sa-Latn">samādhau</i> |
| <a id="dhatu-01-0602"></a>`01.0602` | <i lang="sa-Latn">√kīla~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0603"></a>`01.0603` | <i lang="sa-Latn">√kūla~</i> | <i lang="sa-Latn">āvaraṇe</i> |
| <a id="dhatu-01-0604"></a>`01.0604` | <i lang="sa-Latn">√śūla~</i> | <i lang="sa-Latn">rujāyāṃ saṅghāte saṅkoṣe ca</i> |
| <a id="dhatu-01-0605"></a>`01.0605` | <i lang="sa-Latn">√tūla~</i> | <i lang="sa-Latn">niṣkarṣe</i> |
| <a id="dhatu-01-0606"></a>`01.0606` | <i lang="sa-Latn">√pūla~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0607"></a>`01.0607` | <i lang="sa-Latn">√mūla~</i> | <i lang="sa-Latn">pratiṣṭhāyām</i> |
| <a id="dhatu-01-0608"></a>`01.0608` | <i lang="sa-Latn">√phala~</i> | <i lang="sa-Latn">niṣpattau</i> |
| <a id="dhatu-01-0609"></a>`01.0609` | <i lang="sa-Latn">√culla~</i> | <i lang="sa-Latn">bhāvakaraṇe</i> |
| <a id="dhatu-01-0610"></a>`01.0610` | <i lang="sa-Latn">√phulla~</i> | <i lang="sa-Latn">vikasane</i> |
| <a id="dhatu-01-0611"></a>`01.0611` | <i lang="sa-Latn">√cilla~</i> | <i lang="sa-Latn">śaithilye bhāvakaraṇe ca</i> |
| <a id="dhatu-01-0612"></a>`01.0612` | <i lang="sa-Latn">√tila~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0613"></a>`01.0613` | <i lang="sa-Latn">√tilla~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0614"></a>`01.0614` | <i lang="sa-Latn">√velṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0615"></a>`01.0615` | <i lang="sa-Latn">√celṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0616"></a>`01.0616` | <i lang="sa-Latn">√kelṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0617"></a>`01.0617` | <i lang="sa-Latn">√khelṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0618"></a>`01.0618` | <i lang="sa-Latn">√kṣvelṛ~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0619"></a>`01.0619` | <i lang="sa-Latn">√vella~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0620"></a>`01.0620` | <i lang="sa-Latn">√cella~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0621"></a>`01.0621` | <i lang="sa-Latn">√pelṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0622"></a>`01.0622` | <i lang="sa-Latn">√phelṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0623"></a>`01.0623` | <i lang="sa-Latn">√śelṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0624"></a>`01.0624` | <i lang="sa-Latn">√ṣelṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0625"></a>`01.0625` | <i lang="sa-Latn">√skhala~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-01-0626"></a>`01.0626` | <i lang="sa-Latn">√khala~</i> | <i lang="sa-Latn">sañcaye calane ca</i> |
| <a id="dhatu-01-0627"></a>`01.0627` | <i lang="sa-Latn">√gala~</i> | <i lang="sa-Latn">adane sravaṇe ca</i> |
| <a id="dhatu-01-0628"></a>`01.0628` | <i lang="sa-Latn">√ṣala~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0629"></a>`01.0629` | <i lang="sa-Latn">√dala~</i> | <i lang="sa-Latn">viśaraṇe vidāraṇe ca</i> |
| <a id="dhatu-01-0630"></a>`01.0630` | <i lang="sa-Latn">√śvala~</i> | <i lang="sa-Latn">āśugamane</i> |
| <a id="dhatu-01-0631"></a>`01.0631` | <i lang="sa-Latn">√śvalla~</i> | <i lang="sa-Latn">āśugamane</i> |
| <a id="dhatu-01-0632"></a>`01.0632` | <i lang="sa-Latn">√kholṛ~</i> | <i lang="sa-Latn">gatipratighāte</i> |
| <a id="dhatu-01-0633"></a>`01.0633` | <i lang="sa-Latn">√khorṛ~</i> | <i lang="sa-Latn">gatipratighāte</i> |
| <a id="dhatu-01-0634"></a>`01.0634` | <i lang="sa-Latn">√dhorṛ~</i> | <i lang="sa-Latn">gaticāturye</i> |
| <a id="dhatu-01-0635"></a>`01.0635` | <i lang="sa-Latn">√tsara~</i> | <i lang="sa-Latn">chadmagatau</i> |
| <a id="dhatu-01-0636"></a>`01.0636` | <i lang="sa-Latn">√kmara~</i> | <i lang="sa-Latn">hūrchane</i> |
| <a id="dhatu-01-0637"></a>`01.0637` | <i lang="sa-Latn">√abhra~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0638"></a>`01.0638` | <i lang="sa-Latn">√vabhra~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0639"></a>`01.0639` | <i lang="sa-Latn">√mabhra~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0640"></a>`01.0640` | <i lang="sa-Latn">√cara~</i> | <i lang="sa-Latn">gatau bhakṣaṇe ca</i> |
| <a id="dhatu-01-0641"></a>`01.0641` | <i lang="sa-Latn">√ṣṭhivu~</i> | <i lang="sa-Latn">nirasane</i> |
| <a id="dhatu-01-0642"></a>`01.0642` | <i lang="sa-Latn">√ji\</i> | <i lang="sa-Latn">jaye</i> |
| <a id="dhatu-01-0643"></a>`01.0643` | <i lang="sa-Latn">√jīva~</i> | <i lang="sa-Latn">prāṇadhāraṇe</i> |
| <a id="dhatu-01-0644"></a>`01.0644` | <i lang="sa-Latn">√pīva~</i> | <i lang="sa-Latn">sthaulye</i> |
| <a id="dhatu-01-0645"></a>`01.0645` | <i lang="sa-Latn">√mīva~</i> | <i lang="sa-Latn">sthaulye</i> |
| <a id="dhatu-01-0646"></a>`01.0646` | <i lang="sa-Latn">√tīva~</i> | <i lang="sa-Latn">sthaulye</i> |
| <a id="dhatu-01-0647"></a>`01.0647` | <i lang="sa-Latn">√ṇīva~</i> | <i lang="sa-Latn">sthaulye</i> |
| <a id="dhatu-01-0648"></a>`01.0648` | <i lang="sa-Latn">√kṣivu~</i> | <i lang="sa-Latn">nirasane</i> |
| <a id="dhatu-01-0649"></a>`01.0649` | <i lang="sa-Latn">√kṣevu~</i> | <i lang="sa-Latn">nirasane</i> |
| <a id="dhatu-01-0650"></a>`01.0650` | <i lang="sa-Latn">√urvī~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0651"></a>`01.0651` | <i lang="sa-Latn">√turvī~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0652"></a>`01.0652` | <i lang="sa-Latn">√thurvī~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0653"></a>`01.0653` | <i lang="sa-Latn">√durvī~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0654"></a>`01.0654` | <i lang="sa-Latn">√dhurvī~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0655"></a>`01.0655` | <i lang="sa-Latn">√gurvī~</i> | <i lang="sa-Latn">udyamane</i> |
| <a id="dhatu-01-0656"></a>`01.0656` | <i lang="sa-Latn">√murvī~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0657"></a>`01.0657` | <i lang="sa-Latn">√purva~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-01-0658"></a>`01.0658` | <i lang="sa-Latn">√parva~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-01-0659"></a>`01.0659` | <i lang="sa-Latn">√marva~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-01-0660"></a>`01.0660` | <i lang="sa-Latn">√carva~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0661"></a>`01.0661` | <i lang="sa-Latn">√bharva~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0662"></a>`01.0662` | <i lang="sa-Latn">√parṣa~\</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-01-0663"></a>`01.0663` | <i lang="sa-Latn">√bahi~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0664"></a>`01.0664` | <i lang="sa-Latn">√karva~</i> | <i lang="sa-Latn">darpe</i> |
| <a id="dhatu-01-0665"></a>`01.0665` | <i lang="sa-Latn">√kharva~</i> | <i lang="sa-Latn">darpe</i> |
| <a id="dhatu-01-0666"></a>`01.0666` | <i lang="sa-Latn">√garva~</i> | <i lang="sa-Latn">darpe</i> |
| <a id="dhatu-01-0667"></a>`01.0667` | <i lang="sa-Latn">√arva~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0668"></a>`01.0668` | <i lang="sa-Latn">√śarva~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0669"></a>`01.0669` | <i lang="sa-Latn">√ṣarva~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0670"></a>`01.0670` | <i lang="sa-Latn">√ivi~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-01-0671"></a>`01.0671` | <i lang="sa-Latn">√pivi~</i> | <i lang="sa-Latn">sevane secane ca</i> |
| <a id="dhatu-01-0672"></a>`01.0672` | <i lang="sa-Latn">√mivi~</i> | <i lang="sa-Latn">sevane secane saṃsrane ca</i> |
| <a id="dhatu-01-0673"></a>`01.0673` | <i lang="sa-Latn">√ṇivi~</i> | <i lang="sa-Latn">sevane secane saṃsrane ca</i> |
| <a id="dhatu-01-0674"></a>`01.0674` | <i lang="sa-Latn">√ṣivi~</i> | <i lang="sa-Latn">sevane secane ca</i> |
| <a id="dhatu-01-0675"></a>`01.0675` | <i lang="sa-Latn">√hivi~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-01-0676"></a>`01.0676` | <i lang="sa-Latn">√divi~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-01-0677"></a>`01.0677` | <i lang="sa-Latn">√dhivi~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-01-0678"></a>`01.0678` | <i lang="sa-Latn">√jivi~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-01-0679"></a>`01.0679` | <i lang="sa-Latn">√rivi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0680"></a>`01.0680` | <i lang="sa-Latn">√ravi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0681"></a>`01.0681` | <i lang="sa-Latn">√dhavi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0682"></a>`01.0682` | <i lang="sa-Latn">√kṛvi~</i> | <i lang="sa-Latn">gatau hiṃsākaraṇayośca</i> |
| <a id="dhatu-01-0683"></a>`01.0683` | <i lang="sa-Latn">√mava~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-0684"></a>`01.0684` | <i lang="sa-Latn">√ava~</i> | <i lang="sa-Latn">rakṣaṇagatikāntiprītitṛptyavagamapraveśaśravaṇasvāmyarthayācanakriyecchādīptyavāptyāliṅganahiṃsādānabhāgavṛddhiṣu</i> |
| <a id="dhatu-01-0685"></a>`01.0685` | <i lang="sa-Latn">√dhāvu~^</i> | <i lang="sa-Latn">gatiśuddhyoḥ</i> |
| <a id="dhatu-01-0686"></a>`01.0686` | <i lang="sa-Latn">√dhukṣa~\</i> | <i lang="sa-Latn">sandīpanakleśanajīvaneṣu</i> |
| <a id="dhatu-01-0687"></a>`01.0687` | <i lang="sa-Latn">√dhikṣa~\</i> | <i lang="sa-Latn">sandīpanakleśanajīvaneṣu</i> |
| <a id="dhatu-01-0688"></a>`01.0688` | <i lang="sa-Latn">√vṛkṣa~\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-01-0689"></a>`01.0689` | <i lang="sa-Latn">√śikṣa~\</i> | <i lang="sa-Latn">vidyopādāne</i> |
| <a id="dhatu-01-0690"></a>`01.0690` | <i lang="sa-Latn">√bhikṣa~\</i> | <i lang="sa-Latn">bhikṣāyāmalābhe lābhe ca</i> |
| <a id="dhatu-01-0691"></a>`01.0691` | <i lang="sa-Latn">√kleśa~\</i> | <i lang="sa-Latn">avyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0692"></a>`01.0692` | <i lang="sa-Latn">√dakṣa~\</i> | <i lang="sa-Latn">vṛddhau śīghrārthe ca</i> |
| <a id="dhatu-01-0693"></a>`01.0693` | <i lang="sa-Latn">√dīkṣa~\</i> | <i lang="sa-Latn">mauṇḍyejyopanayananiyamavratādeśeṣu</i> |
| <a id="dhatu-01-0694"></a>`01.0694` | <i lang="sa-Latn">√īkṣa~\</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-01-0695"></a>`01.0695` | <i lang="sa-Latn">√īṣa~\</i> | <i lang="sa-Latn">gatihiṃsādarśaneṣu</i> |
| <a id="dhatu-01-0696"></a>`01.0696` | <i lang="sa-Latn">√bhāṣa~\</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-0697"></a>`01.0697` | <i lang="sa-Latn">√varṣa~\</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-01-0698"></a>`01.0698` | <i lang="sa-Latn">√geṣṛ~\</i> | <i lang="sa-Latn">anvicchāyām</i> |
| <a id="dhatu-01-0699"></a>`01.0699` | <i lang="sa-Latn">√gleṣṛ~\</i> | <i lang="sa-Latn">anvicchāyām</i> |
| <a id="dhatu-01-0700"></a>`01.0700` | <i lang="sa-Latn">√peṣṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0701"></a>`01.0701` | <i lang="sa-Latn">√eṣṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0702"></a>`01.0702` | <i lang="sa-Latn">√yeṣṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0703"></a>`01.0703` | <i lang="sa-Latn">√jeṣṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0704"></a>`01.0704` | <i lang="sa-Latn">√ṇeṣṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0705"></a>`01.0705` | <i lang="sa-Latn">√eṣṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0706"></a>`01.0706` | <i lang="sa-Latn">√preṣṛ~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0707"></a>`01.0707` | <i lang="sa-Latn">√reṣṛ~\</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0708"></a>`01.0708` | <i lang="sa-Latn">√heṣṛ~\</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0709"></a>`01.0709` | <i lang="sa-Latn">√hreṣṛ~\</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0710"></a>`01.0710` | <i lang="sa-Latn">√kāsṛ~\</i> | <i lang="sa-Latn">śabdakutsāyām</i> |
| <a id="dhatu-01-0711"></a>`01.0711` | <i lang="sa-Latn">√bhāsṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0712"></a>`01.0712` | <i lang="sa-Latn">√ṇāsṛ~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0713"></a>`01.0713` | <i lang="sa-Latn">√rāsṛ~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0714"></a>`01.0714` | <i lang="sa-Latn">√ṇasa~\</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-01-0715"></a>`01.0715` | <i lang="sa-Latn">√bhyasa~\</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-01-0716"></a>`01.0716` | <i lang="sa-Latn">√śasi~\</i> | <i lang="sa-Latn">icchāyām</i> |
| <a id="dhatu-01-0717"></a>`01.0717` | <i lang="sa-Latn">√grasu~\</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0718"></a>`01.0718` | <i lang="sa-Latn">√glasu~\</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0719"></a>`01.0719` | <i lang="sa-Latn">√īha~\</i> | <i lang="sa-Latn">ceṣṭāyām</i> |
| <a id="dhatu-01-0720"></a>`01.0720` | <i lang="sa-Latn">√vahi~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0721"></a>`01.0721` | <i lang="sa-Latn">√mahi~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0722"></a>`01.0722` | <i lang="sa-Latn">√ahi~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0723"></a>`01.0723` | <i lang="sa-Latn">√garha~\</i> | <i lang="sa-Latn">kutsāyām</i> |
| <a id="dhatu-01-0724"></a>`01.0724` | <i lang="sa-Latn">√galha~\</i> | <i lang="sa-Latn">kutsāyām</i> |
| <a id="dhatu-01-0725"></a>`01.0725` | <i lang="sa-Latn">√barha~\</i> | <i lang="sa-Latn">prādhānye</i> |
| <a id="dhatu-01-0726"></a>`01.0726` | <i lang="sa-Latn">√balha~\</i> | <i lang="sa-Latn">prādhānye</i> |
| <a id="dhatu-01-0727"></a>`01.0727` | <i lang="sa-Latn">√varha~\</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsācchādaneṣu</i> |
| <a id="dhatu-01-0728"></a>`01.0728` | <i lang="sa-Latn">√valha~\</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsācchādaneṣu</i> |
| <a id="dhatu-01-0729"></a>`01.0729` | <i lang="sa-Latn">√pliha~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0730"></a>`01.0730` | <i lang="sa-Latn">√vehṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0731"></a>`01.0731` | <i lang="sa-Latn">√jehṛ~\</i> | <i lang="sa-Latn">prayatne gatau ca</i> |
| <a id="dhatu-01-0732"></a>`01.0732` | <i lang="sa-Latn">√bāhṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0733"></a>`01.0733` | <i lang="sa-Latn">√drāhṛ~\</i> | <i lang="sa-Latn">nidrākṣaye nikṣepe ca</i> |
| <a id="dhatu-01-0734"></a>`01.0734` | <i lang="sa-Latn">√kāśṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0735"></a>`01.0735` | <i lang="sa-Latn">√ūha~\</i> | <i lang="sa-Latn">vitarke</i> |
| <a id="dhatu-01-0736"></a>`01.0736` | <i lang="sa-Latn">√gāhū~\</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-01-0737"></a>`01.0737` | <i lang="sa-Latn">√gṛhū~\</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-01-0738"></a>`01.0738` | <i lang="sa-Latn">√glaha~\</i> | <i lang="sa-Latn">grahaṇe apādāne ca</i> |
| <a id="dhatu-01-0739"></a>`01.0739` | <i lang="sa-Latn">√ghaṣa~\</i> | <i lang="sa-Latn">kāntikaraṇe</i> |
| <a id="dhatu-01-0740"></a>`01.0740` | <i lang="sa-Latn">√ghuṣi~\</i> | <i lang="sa-Latn">kāntikaraṇe</i> |
| <a id="dhatu-01-0741"></a>`01.0741` | <i lang="sa-Latn">√ghuṣi~r</i> | <i lang="sa-Latn">aviśabdane</i> |
| <a id="dhatu-01-0742"></a>`01.0742` | <i lang="sa-Latn">√akṣū~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-01-0743"></a>`01.0743` | <i lang="sa-Latn">√takṣū~</i> | <i lang="sa-Latn">tanūkaraṇe</i> |
| <a id="dhatu-01-0744"></a>`01.0744` | <i lang="sa-Latn">√tvakṣū~</i> | <i lang="sa-Latn">tanūkaraṇe</i> |
| <a id="dhatu-01-0745"></a>`01.0745` | <i lang="sa-Latn">√ukṣa~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0746"></a>`01.0746` | <i lang="sa-Latn">√rakṣa~</i> | <i lang="sa-Latn">pālane</i> |
| <a id="dhatu-01-0747"></a>`01.0747` | <i lang="sa-Latn">√ṇikṣa~</i> | <i lang="sa-Latn">cumbane</i> |
| <a id="dhatu-01-0748"></a>`01.0748` | <i lang="sa-Latn">√trakṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0749"></a>`01.0749` | <i lang="sa-Latn">√ṣṭrakṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0750"></a>`01.0750` | <i lang="sa-Latn">√tṛkṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0751"></a>`01.0751` | <i lang="sa-Latn">√ṣṭṛkṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0752"></a>`01.0752` | <i lang="sa-Latn">√ṇakṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0753"></a>`01.0753` | <i lang="sa-Latn">√vakṣa~</i> | <i lang="sa-Latn">roṣe saṅghāte ca</i> |
| <a id="dhatu-01-0754"></a>`01.0754` | <i lang="sa-Latn">√mṛkṣa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0755"></a>`01.0755` | <i lang="sa-Latn">√mrakṣa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-01-0756"></a>`01.0756` | <i lang="sa-Latn">√takṣa~</i> | <i lang="sa-Latn">tvacane</i> |
| <a id="dhatu-01-0757"></a>`01.0757` | <i lang="sa-Latn">√pakṣa~</i> | <i lang="sa-Latn">parigrahe</i> |
| <a id="dhatu-01-0758"></a>`01.0758` | <i lang="sa-Latn">√sūrkṣa~</i> | <i lang="sa-Latn">ādare</i> |
| <a id="dhatu-01-0759"></a>`01.0759` | <i lang="sa-Latn">√ṣalṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0760"></a>`01.0760` | <i lang="sa-Latn">√kākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām</i> |
| <a id="dhatu-01-0761"></a>`01.0761` | <i lang="sa-Latn">√vākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām</i> |
| <a id="dhatu-01-0762"></a>`01.0762` | <i lang="sa-Latn">√mākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām</i> |
| <a id="dhatu-01-0763"></a>`01.0763` | <i lang="sa-Latn">√drākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām ghoravāśite ca</i> |
| <a id="dhatu-01-0764"></a>`01.0764` | <i lang="sa-Latn">√dhrākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām ghoravāśite ca</i> |
| <a id="dhatu-01-0765"></a>`01.0765` | <i lang="sa-Latn">√dhvākṣi~</i> | <i lang="sa-Latn">kāṅkṣāyām ghoravāśite ca</i> |
| <a id="dhatu-01-0766"></a>`01.0766` | <i lang="sa-Latn">√śucyī~</i> | <i lang="sa-Latn">abhiṣave</i> |
| <a id="dhatu-01-0767"></a>`01.0767` | <i lang="sa-Latn">√cūṣa~</i> | <i lang="sa-Latn">pāne</i> |
| <a id="dhatu-01-0768"></a>`01.0768` | <i lang="sa-Latn">√tūṣa~</i> | <i lang="sa-Latn">tuṣṭau</i> |
| <a id="dhatu-01-0769"></a>`01.0769` | <i lang="sa-Latn">√pūṣa~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0770"></a>`01.0770` | <i lang="sa-Latn">√mūṣa~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-01-0771"></a>`01.0771` | <i lang="sa-Latn">√lūṣa~</i> | <i lang="sa-Latn">bhūṣāyām</i> |
| <a id="dhatu-01-0772"></a>`01.0772` | <i lang="sa-Latn">√rūṣa~</i> | <i lang="sa-Latn">bhūṣāyām</i> |
| <a id="dhatu-01-0773"></a>`01.0773` | <i lang="sa-Latn">√śūṣa~</i> | <i lang="sa-Latn">prasave</i> |
| <a id="dhatu-01-0774"></a>`01.0774` | <i lang="sa-Latn">√ṣūṣa~</i> | <i lang="sa-Latn">prasave</i> |
| <a id="dhatu-01-0775"></a>`01.0775` | <i lang="sa-Latn">√yūṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0776"></a>`01.0776` | <i lang="sa-Latn">√jūṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0777"></a>`01.0777` | <i lang="sa-Latn">√bhūṣa~</i> | <i lang="sa-Latn">alaṅkāre</i> |
| <a id="dhatu-01-0778"></a>`01.0778` | <i lang="sa-Latn">√gluhū~^</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-01-0779"></a>`01.0779` | <i lang="sa-Latn">√ūṣa~</i> | <i lang="sa-Latn">rujāyām</i> |
| <a id="dhatu-01-0780"></a>`01.0780` | <i lang="sa-Latn">√īṣa~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-01-0781"></a>`01.0781` | <i lang="sa-Latn">√kaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0782"></a>`01.0782` | <i lang="sa-Latn">√khaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0783"></a>`01.0783` | <i lang="sa-Latn">√śi\ṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0784"></a>`01.0784` | <i lang="sa-Latn">√jaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0785"></a>`01.0785` | <i lang="sa-Latn">√jhaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0786"></a>`01.0786` | <i lang="sa-Latn">√śaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0787"></a>`01.0787` | <i lang="sa-Latn">√vaṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0788"></a>`01.0788` | <i lang="sa-Latn">√maṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0789"></a>`01.0789` | <i lang="sa-Latn">√ruṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0790"></a>`01.0790` | <i lang="sa-Latn">√riṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0791"></a>`01.0791` | <i lang="sa-Latn">√bhaṣa~</i> | <i lang="sa-Latn">bhartsane</i> |
| <a id="dhatu-01-0792"></a>`01.0792` | <i lang="sa-Latn">√uṣa~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0793"></a>`01.0793` | <i lang="sa-Latn">√jiṣu~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0794"></a>`01.0794` | <i lang="sa-Latn">√vi\ṣu~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0795"></a>`01.0795` | <i lang="sa-Latn">√miṣu~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0796"></a>`01.0796` | <i lang="sa-Latn">√muṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0797"></a>`01.0797` | <i lang="sa-Latn">√puṣa~</i> | <i lang="sa-Latn">puṣṭau</i> |
| <a id="dhatu-01-0798"></a>`01.0798` | <i lang="sa-Latn">√śriṣu~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0799"></a>`01.0799` | <i lang="sa-Latn">√śliṣu~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0800"></a>`01.0800` | <i lang="sa-Latn">√pruṣu~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0801"></a>`01.0801` | <i lang="sa-Latn">√pluṣu~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-01-0802"></a>`01.0802` | <i lang="sa-Latn">√pṛṣu~</i> | <i lang="sa-Latn">secanahiṃsāsaṅkleśaneṣu</i> |
| <a id="dhatu-01-0803"></a>`01.0803` | <i lang="sa-Latn">√vṛṣu~</i> | <i lang="sa-Latn">secanahiṃsāsaṅkleśaneṣu</i> |
| <a id="dhatu-01-0804"></a>`01.0804` | <i lang="sa-Latn">√mṛṣu~</i> | <i lang="sa-Latn">secane sahane ca</i> |
| <a id="dhatu-01-0805"></a>`01.0805` | <i lang="sa-Latn">√ghṛṣu~</i> | <i lang="sa-Latn">saṅgharṣe</i> |
| <a id="dhatu-01-0806"></a>`01.0806` | <i lang="sa-Latn">√hṛṣu~</i> | <i lang="sa-Latn">alīke</i> |
| <a id="dhatu-01-0807"></a>`01.0807` | <i lang="sa-Latn">√tusa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0808"></a>`01.0808` | <i lang="sa-Latn">√hrasa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0809"></a>`01.0809` | <i lang="sa-Latn">√hlasa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0810"></a>`01.0810` | <i lang="sa-Latn">√rasa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0811"></a>`01.0811` | <i lang="sa-Latn">√lasa~</i> | <i lang="sa-Latn">śleṣaṇakrīḍanayoḥ</i> |
| <a id="dhatu-01-0812"></a>`01.0812` | <i lang="sa-Latn">√gha\sḷ~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-0813"></a>`01.0813` | <i lang="sa-Latn">√jarja~</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsātarjaneṣu</i> |
| <a id="dhatu-01-0814"></a>`01.0814` | <i lang="sa-Latn">√carca~</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsātarjaneṣu</i> |
| <a id="dhatu-01-0815"></a>`01.0815` | <i lang="sa-Latn">√jharjha~</i> | <i lang="sa-Latn">paribhāṣaṇahiṃsātarjaneṣu</i> |
| <a id="dhatu-01-0816"></a>`01.0816` | <i lang="sa-Latn">√pisṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0817"></a>`01.0817` | <i lang="sa-Latn">√pesṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0818"></a>`01.0818` | <i lang="sa-Latn">√visṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0819"></a>`01.0819` | <i lang="sa-Latn">√vesṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0820"></a>`01.0820` | <i lang="sa-Latn">√piśṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0821"></a>`01.0821` | <i lang="sa-Latn">√peśṛ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0822"></a>`01.0822` | <i lang="sa-Latn">√hase~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0823"></a>`01.0823` | <i lang="sa-Latn">√ṇiśa~</i> | <i lang="sa-Latn">samādhau</i> |
| <a id="dhatu-01-0824"></a>`01.0824` | <i lang="sa-Latn">√miśa~</i> | <i lang="sa-Latn">śabde roṣakṛte gatau ca</i> |
| <a id="dhatu-01-0825"></a>`01.0825` | <i lang="sa-Latn">√maśa~</i> | <i lang="sa-Latn">śabde roṣakṛte gatau ca</i> |
| <a id="dhatu-01-0826"></a>`01.0826` | <i lang="sa-Latn">√śava~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0827"></a>`01.0827` | <i lang="sa-Latn">√śaśa~</i> | <i lang="sa-Latn">plutagatau</i> |
| <a id="dhatu-01-0828"></a>`01.0828` | <i lang="sa-Latn">√śasu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0829"></a>`01.0829` | <i lang="sa-Latn">√śansu~</i> | <i lang="sa-Latn">stutau</i> |
| <a id="dhatu-01-0830"></a>`01.0830` | <i lang="sa-Latn">√caha~</i> | <i lang="sa-Latn">parikalkane</i> |
| <a id="dhatu-01-0831"></a>`01.0831` | <i lang="sa-Latn">√maha~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-01-0832"></a>`01.0832` | <i lang="sa-Latn">√raha~</i> | <i lang="sa-Latn">tyāge</i> |
| <a id="dhatu-01-0833"></a>`01.0833` | <i lang="sa-Latn">√rahi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0834"></a>`01.0834` | <i lang="sa-Latn">√dṛha~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0835"></a>`01.0835` | <i lang="sa-Latn">√dṛhi~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0836"></a>`01.0836` | <i lang="sa-Latn">√bṛha~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0837"></a>`01.0837` | <i lang="sa-Latn">√bṛhi~</i> | <i lang="sa-Latn">vṛddhau śabde ca</i> |
| <a id="dhatu-01-0838"></a>`01.0838` | <i lang="sa-Latn">√tuhi~r</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-01-0839"></a>`01.0839` | <i lang="sa-Latn">√duhi~r</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-01-0840"></a>`01.0840` | <i lang="sa-Latn">√uhi~r</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-01-0841"></a>`01.0841` | <i lang="sa-Latn">√arha~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-01-0842"></a>`01.0842` | <i lang="sa-Latn">√dyuta~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0843"></a>`01.0843` | <i lang="sa-Latn">√śvitā~\</i> | <i lang="sa-Latn">varṇe</i> |
| <a id="dhatu-01-0844"></a>`01.0844` | <i lang="sa-Latn">√ñimidā~\</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-01-0845"></a>`01.0845` | <i lang="sa-Latn">√ñiṣvidā~\</i> | <i lang="sa-Latn">snehanamocanayoḥ gātraprasravaṇe ca</i> |
| <a id="dhatu-01-0846"></a>`01.0846` | <i lang="sa-Latn">√ñikṣvidā~\</i> | <i lang="sa-Latn">snehanamocanayoḥ</i> |
| <a id="dhatu-01-0847"></a>`01.0847` | <i lang="sa-Latn">√ruca~\</i> | <i lang="sa-Latn">dīptāvabhiprītau ca</i> |
| <a id="dhatu-01-0848"></a>`01.0848` | <i lang="sa-Latn">√ghuṭa~\</i> | <i lang="sa-Latn">parivartane</i> |
| <a id="dhatu-01-0849"></a>`01.0849` | <i lang="sa-Latn">√ruṭa~\</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-01-0850"></a>`01.0850` | <i lang="sa-Latn">√luṭa~\</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-01-0851"></a>`01.0851` | <i lang="sa-Latn">√luṭha~\</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-01-0852"></a>`01.0852` | <i lang="sa-Latn">√vṛha~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0853"></a>`01.0853` | <i lang="sa-Latn">√śubha~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0854"></a>`01.0854` | <i lang="sa-Latn">√kṣubha~\</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-01-0855"></a>`01.0855` | <i lang="sa-Latn">√ṇabha~\</i> | <i lang="sa-Latn">hiṃsāyām abhāve ca</i> |
| <a id="dhatu-01-0856"></a>`01.0856` | <i lang="sa-Latn">√tubha~\</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0857"></a>`01.0857` | <i lang="sa-Latn">√sransu~\</i> | <i lang="sa-Latn">avasraṃsane</i> |
| <a id="dhatu-01-0858"></a>`01.0858` | <i lang="sa-Latn">√dhvansu~\</i> | <i lang="sa-Latn">avasraṃsane gatau ca</i> |
| <a id="dhatu-01-0859"></a>`01.0859` | <i lang="sa-Latn">√bhransu~\</i> | <i lang="sa-Latn">avasraṃsane</i> |
| <a id="dhatu-01-0860"></a>`01.0860` | <i lang="sa-Latn">√bhranśu~\</i> | <i lang="sa-Latn">avasraṃsane</i> |
| <a id="dhatu-01-0861"></a>`01.0861` | <i lang="sa-Latn">√sranbhu~\</i> | <i lang="sa-Latn">viśvāse</i> |
| <a id="dhatu-01-0862"></a>`01.0862` | <i lang="sa-Latn">√vṛtu~\</i> | <i lang="sa-Latn">vartane</i> |
| <a id="dhatu-01-0863"></a>`01.0863` | <i lang="sa-Latn">√vṛdhu~\</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0864"></a>`01.0864` | <i lang="sa-Latn">√śṛdhu~\</i> | <i lang="sa-Latn">undane śabdakutsāyām ca</i> |
| <a id="dhatu-01-0865"></a>`01.0865` | <i lang="sa-Latn">√syandū~\</i> | <i lang="sa-Latn">prasravaṇe</i> |
| <a id="dhatu-01-0866"></a>`01.0866` | <i lang="sa-Latn">√kṛpū~\</i> | <i lang="sa-Latn">sāmarthye</i> |
| <a id="dhatu-01-0867"></a>`01.0867` | <i lang="sa-Latn">√ghaṭa~\</i> | <i lang="sa-Latn">ceṣṭāyām</i> |
| <a id="dhatu-01-0868"></a>`01.0868` | <i lang="sa-Latn">√vyatha~\</i> | <i lang="sa-Latn">bhayasañcalanayoḥ</i> |
| <a id="dhatu-01-0869"></a>`01.0869` | <i lang="sa-Latn">√pratha~\</i> | <i lang="sa-Latn">prakhyāne</i> |
| <a id="dhatu-01-0870"></a>`01.0870` | <i lang="sa-Latn">√prasa~\</i> | <i lang="sa-Latn">vistāre</i> |
| <a id="dhatu-01-0871"></a>`01.0871` | <i lang="sa-Latn">√mrada~\</i> | <i lang="sa-Latn">mardane</i> |
| <a id="dhatu-01-0872"></a>`01.0872` | <i lang="sa-Latn">√skhada~\</i> | <i lang="sa-Latn">skhadane</i> |
| <a id="dhatu-01-0873"></a>`01.0873` | <i lang="sa-Latn">√kṣaji~\</i> | <i lang="sa-Latn">gatidānayoḥ</i> |
| <a id="dhatu-01-0874"></a>`01.0874` | <i lang="sa-Latn">√dakṣa~\</i> | <i lang="sa-Latn">gatihiṃsanaśāsanavṛddhiśīghrārtheṣu</i> |
| <a id="dhatu-01-0875"></a>`01.0875` | <i lang="sa-Latn">√kṛpa~\</i> | <i lang="sa-Latn">kṛpāyāṃ gatau ca</i> |
| <a id="dhatu-01-0876"></a>`01.0876` | <i lang="sa-Latn">√krapa~\</i> | <i lang="sa-Latn">kṛpāyāṃ gatau ca</i> |
| <a id="dhatu-01-0877"></a>`01.0877` | <i lang="sa-Latn">√vṛhi~</i> | <i lang="sa-Latn">vṛddhau śabde ca</i> |
| <a id="dhatu-01-0878"></a>`01.0878` | <i lang="sa-Latn">√kadi~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0879"></a>`01.0879` | <i lang="sa-Latn">√kradi~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0880"></a>`01.0880` | <i lang="sa-Latn">√kladi~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0881"></a>`01.0881` | <i lang="sa-Latn">√kada~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0882"></a>`01.0882` | <i lang="sa-Latn">√krada~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0883"></a>`01.0883` | <i lang="sa-Latn">√klada~\</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0884"></a>`01.0884` | <i lang="sa-Latn">√ñitvarā~\</i> | <i lang="sa-Latn">sambhrame</i> |
| <a id="dhatu-01-0885"></a>`01.0885` | <i lang="sa-Latn">√jvara~</i> | <i lang="sa-Latn">roge</i> |
| <a id="dhatu-01-0886"></a>`01.0886` | <i lang="sa-Latn">√gaḍa~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-0887"></a>`01.0887` | <i lang="sa-Latn">√heḍa~</i> | <i lang="sa-Latn">veṣṭane</i> |
| <a id="dhatu-01-0888"></a>`01.0888` | <i lang="sa-Latn">√vaṭa~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0889"></a>`01.0889` | <i lang="sa-Latn">√bhaṭa~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-0890"></a>`01.0890` | <i lang="sa-Latn">√ṇaṭa~</i> | <i lang="sa-Latn">nṛttau gatau ca</i> |
| <a id="dhatu-01-0891"></a>`01.0891` | <i lang="sa-Latn">√ṣṭaka~</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-01-0892"></a>`01.0892` | <i lang="sa-Latn">√caka~</i> | <i lang="sa-Latn">tṛptau</i> |
| <a id="dhatu-01-0893"></a>`01.0893` | <i lang="sa-Latn">√kakhe~</i> | <i lang="sa-Latn">hasane</i> |
| <a id="dhatu-01-0894"></a>`01.0894` | <i lang="sa-Latn">√rage~</i> | <i lang="sa-Latn">śaṅkāyām</i> |
| <a id="dhatu-01-0895"></a>`01.0895` | <i lang="sa-Latn">√lage~</i> | <i lang="sa-Latn">saṅge</i> |
| <a id="dhatu-01-0896"></a>`01.0896` | <i lang="sa-Latn">√hrage~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-0897"></a>`01.0897` | <i lang="sa-Latn">√hlage~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-0898"></a>`01.0898` | <i lang="sa-Latn">√ṣage~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-0899"></a>`01.0899` | <i lang="sa-Latn">√ṣṭage~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-0900"></a>`01.0900` | <i lang="sa-Latn">√kage~</i> | <i lang="sa-Latn">anekārthāḥ</i> |
| <a id="dhatu-01-0901"></a>`01.0901` | <i lang="sa-Latn">√aka~</i> | <i lang="sa-Latn">kuṭilāyāṃ gatau</i> |
| <a id="dhatu-01-0902"></a>`01.0902` | <i lang="sa-Latn">√aga~</i> | <i lang="sa-Latn">kuṭilāyāṃ gatau</i> |
| <a id="dhatu-01-0903"></a>`01.0903` | <i lang="sa-Latn">√kaṇa~</i> | <i lang="sa-Latn">gatau śabde ca</i> |
| <a id="dhatu-01-0904"></a>`01.0904` | <i lang="sa-Latn">√raṇa~</i> | <i lang="sa-Latn">gatau śabde ca</i> |
| <a id="dhatu-01-0905"></a>`01.0905` | <i lang="sa-Latn">√caṇa~</i> | <i lang="sa-Latn">dāne gatau ca</i> |
| <a id="dhatu-01-0906"></a>`01.0906` | <i lang="sa-Latn">√śaṇa~</i> | <i lang="sa-Latn">dāne gatau ca</i> |
| <a id="dhatu-01-0907"></a>`01.0907` | <i lang="sa-Latn">√śraṇa~</i> | <i lang="sa-Latn">dāne gatau ca</i> |
| <a id="dhatu-01-0908"></a>`01.0908` | <i lang="sa-Latn">√śratha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0909"></a>`01.0909` | <i lang="sa-Latn">√ṣṭhage~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-0910"></a>`01.0910` | <i lang="sa-Latn">√ślatha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0911"></a>`01.0911` | <i lang="sa-Latn">√knatha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0912"></a>`01.0912` | <i lang="sa-Latn">√kratha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0913"></a>`01.0913` | <i lang="sa-Latn">√klatha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0914"></a>`01.0914` | <i lang="sa-Latn">√cana~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0915"></a>`01.0915` | <i lang="sa-Latn">√vana~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-0916"></a>`01.0916` | <i lang="sa-Latn">√jvala~</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0917"></a>`01.0917` | <i lang="sa-Latn">√hvala~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0918"></a>`01.0918` | <i lang="sa-Latn">√hmala~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0919"></a>`01.0919` | <i lang="sa-Latn">√smṛ\</i> | <i lang="sa-Latn">ādhyāne</i> |
| <a id="dhatu-01-0920"></a>`01.0920` | <i lang="sa-Latn">√dṝ</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-01-0921"></a>`01.0921` | <i lang="sa-Latn">√nṝ</i> | <i lang="sa-Latn">naye</i> |
| <a id="dhatu-01-0922"></a>`01.0922` | <i lang="sa-Latn">√śrā</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-01-0923"></a>`01.0923` | <i lang="sa-Latn">√jñā</i> | <i lang="sa-Latn">māraṇatoṣaṇaniśāmaneṣu</i> |
| <a id="dhatu-01-0924"></a>`01.0924` | <i lang="sa-Latn">√cala~</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-01-0925"></a>`01.0925` | <i lang="sa-Latn">√chadiḥ</i> | <i lang="sa-Latn">ūrjane</i> |
| <a id="dhatu-01-0926"></a>`01.0926` | <i lang="sa-Latn">√laḍa~</i> | <i lang="sa-Latn">vilāse jihvonmathane ca</i> |
| <a id="dhatu-01-0927"></a>`01.0927` | <i lang="sa-Latn">√madī~</i> | <i lang="sa-Latn">harṣaglepanayoḥ</i> |
| <a id="dhatu-01-0928"></a>`01.0928` | <i lang="sa-Latn">√dhvana~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0929"></a>`01.0929` | <i lang="sa-Latn">√śamo~</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-01-0930"></a>`01.0930` | <i lang="sa-Latn">√yama~</i> | <i lang="sa-Latn">apariveṣaṇe</i> |
| <a id="dhatu-01-0931"></a>`01.0931` | <i lang="sa-Latn">√skhadi~\r</i> | <i lang="sa-Latn">vidrāvaṇe vidāraṇe ca</i> |
| <a id="dhatu-01-0932"></a>`01.0932` | <i lang="sa-Latn">√svana~</i> | <i lang="sa-Latn">avataṃsane</i> |
| <a id="dhatu-01-0942"></a>`01.0942` | <i lang="sa-Latn">√tṛha~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0943"></a>`01.0943` | <i lang="sa-Latn">√tṛhi~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-0945"></a>`01.0945` | <i lang="sa-Latn">√rugi~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-01-0946"></a>`01.0946` | <i lang="sa-Latn">√khuḍi~</i> | <i lang="sa-Latn">gativaikalye</i> |
| <a id="dhatu-01-0947"></a>`01.0947` | <i lang="sa-Latn">√mleḍṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0948"></a>`01.0948` | <i lang="sa-Latn">√meṭṛ~</i> | <i lang="sa-Latn">unmāde</i> |
| <a id="dhatu-01-0949"></a>`01.0949` | <i lang="sa-Latn">√biḍa~</i> | <i lang="sa-Latn">ākrośe</i> |
| <a id="dhatu-01-0950"></a>`01.0950` | <i lang="sa-Latn">√makṣa~</i> | <i lang="sa-Latn">roṣe saṅghāte ca</i> |
| <a id="dhatu-01-0951"></a>`01.0951` | <i lang="sa-Latn">√vanu~</i> | <i lang="sa-Latn">anekārthatve</i> |
| <a id="dhatu-01-0952"></a>`01.0952` | <i lang="sa-Latn">√vāhṛ~\</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-01-0953"></a>`01.0953` | <i lang="sa-Latn">√ra\ma~\</i> | <i lang="sa-Latn">krīḍāyām</i> |
| <a id="dhatu-01-0954"></a>`01.0954` | <i lang="sa-Latn">√ḍuyācṛ~^</i> | <i lang="sa-Latn">yācñāyām</i> |
| <a id="dhatu-01-0955"></a>`01.0955` | <i lang="sa-Latn">√phaṇa~</i> | <i lang="sa-Latn">gatidīptyoḥ</i> |
| <a id="dhatu-01-0956"></a>`01.0956` | <i lang="sa-Latn">√rājṛ~^</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0957"></a>`01.0957` | <i lang="sa-Latn">√ṭubhrājṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0958"></a>`01.0958` | <i lang="sa-Latn">√ṭubhrāśṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0959"></a>`01.0959` | <i lang="sa-Latn">√ṭubhlāśṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0960"></a>`01.0960` | <i lang="sa-Latn">√syamu~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0961"></a>`01.0961` | <i lang="sa-Latn">√svana~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0962"></a>`01.0962` | <i lang="sa-Latn">√dhvana~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-0963"></a>`01.0963` | <i lang="sa-Latn">√ṣama~</i> | <i lang="sa-Latn">avaikalye</i> |
| <a id="dhatu-01-0964"></a>`01.0964` | <i lang="sa-Latn">√ṣṭama~</i> | <i lang="sa-Latn">avaikalye</i> |
| <a id="dhatu-01-0965"></a>`01.0965` | <i lang="sa-Latn">√jvala~</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-0966"></a>`01.0966` | <i lang="sa-Latn">√cala~</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-01-0967"></a>`01.0967` | <i lang="sa-Latn">√jala~</i> | <i lang="sa-Latn">ghātane</i> |
| <a id="dhatu-01-0968"></a>`01.0968` | <i lang="sa-Latn">√ṭala~</i> | <i lang="sa-Latn">vaiklavye</i> |
| <a id="dhatu-01-0969"></a>`01.0969` | <i lang="sa-Latn">√ṭvala~</i> | <i lang="sa-Latn">vaikalye</i> |
| <a id="dhatu-01-0970"></a>`01.0970` | <i lang="sa-Latn">√ṣṭhala~</i> | <i lang="sa-Latn">sthāne</i> |
| <a id="dhatu-01-0971"></a>`01.0971` | <i lang="sa-Latn">√hala~</i> | <i lang="sa-Latn">vilekhane</i> |
| <a id="dhatu-01-0972"></a>`01.0972` | <i lang="sa-Latn">√ṇala~</i> | <i lang="sa-Latn">gandhe bandhane ca</i> |
| <a id="dhatu-01-0973"></a>`01.0973` | <i lang="sa-Latn">√pala~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0974"></a>`01.0974` | <i lang="sa-Latn">√bala~</i> | <i lang="sa-Latn">prāṇane dhānyāvarodhane ca</i> |
| <a id="dhatu-01-0975"></a>`01.0975` | <i lang="sa-Latn">√pula~</i> | <i lang="sa-Latn">mahattve</i> |
| <a id="dhatu-01-0976"></a>`01.0976` | <i lang="sa-Latn">√kula~</i> | <i lang="sa-Latn">saṃstyāne bandhuṣu ca</i> |
| <a id="dhatu-01-0977"></a>`01.0977` | <i lang="sa-Latn">√śala~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0978"></a>`01.0978` | <i lang="sa-Latn">√hula~</i> | <i lang="sa-Latn">gatau hiṃsāyāṃ saṃvaraṇe ca</i> |
| <a id="dhatu-01-0979"></a>`01.0979` | <i lang="sa-Latn">√patḷ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0980"></a>`01.0980` | <i lang="sa-Latn">√kṣala~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-01-0981"></a>`01.0981` | <i lang="sa-Latn">√kvathe~</i> | <i lang="sa-Latn">niṣpāke</i> |
| <a id="dhatu-01-0982"></a>`01.0982` | <i lang="sa-Latn">√pathe~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0983"></a>`01.0983` | <i lang="sa-Latn">√mathe~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-01-0984"></a>`01.0984` | <i lang="sa-Latn">√ṭuvama~</i> | <i lang="sa-Latn">udgiraṇe</i> |
| <a id="dhatu-01-0985"></a>`01.0985` | <i lang="sa-Latn">√bhramu~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-01-0986"></a>`01.0986` | <i lang="sa-Latn">√kṣara~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-01-0987"></a>`01.0987` | <i lang="sa-Latn">√dvṛ\</i> | <i lang="sa-Latn">sthagane</i> |
| <a id="dhatu-01-0988"></a>`01.0988` | <i lang="sa-Latn">√ṣaha~\</i> | <i lang="sa-Latn">marṣaṇe</i> |
| <a id="dhatu-01-0989"></a>`01.0989` | <i lang="sa-Latn">√ra\mu~\</i> | <i lang="sa-Latn">krīḍāyām</i> |
| <a id="dhatu-01-0990"></a>`01.0990` | <i lang="sa-Latn">√ṣa\dḷ~</i> | <i lang="sa-Latn">viśaraṇagatyavasādaneṣu</i> |
| <a id="dhatu-01-0991"></a>`01.0991` | <i lang="sa-Latn">√śa\dḷ~</i> | <i lang="sa-Latn">śātane</i> |
| <a id="dhatu-01-0992"></a>`01.0992` | <i lang="sa-Latn">√kru\śa~</i> | <i lang="sa-Latn">āhvāne rodane ca</i> |
| <a id="dhatu-01-0993"></a>`01.0993` | <i lang="sa-Latn">√kuca~</i> | <i lang="sa-Latn">samparcanakauṭilyapratiṣṭambhavilekhaneṣu</i> |
| <a id="dhatu-01-0994"></a>`01.0994` | <i lang="sa-Latn">√budha~</i> | <i lang="sa-Latn">avagamane</i> |
| <a id="dhatu-01-0995"></a>`01.0995` | <i lang="sa-Latn">√ru\ha~</i> | <i lang="sa-Latn">bījajanmani prādurbhāve ca</i> |
| <a id="dhatu-01-0996"></a>`01.0996` | <i lang="sa-Latn">√kasa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-0997"></a>`01.0997` | <i lang="sa-Latn">√hikka~^</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-0998"></a>`01.0998` | <i lang="sa-Latn">√ancu~^</i> | <i lang="sa-Latn">gatau yācane ca</i> |
| <a id="dhatu-01-0999"></a>`01.0999` | <i lang="sa-Latn">√acu~^</i> | <i lang="sa-Latn">gatau yācane ca</i> |
| <a id="dhatu-01-1000"></a>`01.1000` | <i lang="sa-Latn">√aci~^</i> | <i lang="sa-Latn">gatau yācane ca</i> |
| <a id="dhatu-01-1001"></a>`01.1001` | <i lang="sa-Latn">√ṭuyācṛ~^</i> | <i lang="sa-Latn">yācñāyām</i> |
| <a id="dhatu-01-1002"></a>`01.1002` | <i lang="sa-Latn">√reṭṛ~^</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-01-1003"></a>`01.1003` | <i lang="sa-Latn">√cate~^</i> | <i lang="sa-Latn">yācane</i> |
| <a id="dhatu-01-1004"></a>`01.1004` | <i lang="sa-Latn">√cade~^</i> | <i lang="sa-Latn">yācane</i> |
| <a id="dhatu-01-1005"></a>`01.1005` | <i lang="sa-Latn">√prothṛ~^</i> | <i lang="sa-Latn">paryāptau</i> |
| <a id="dhatu-01-1006"></a>`01.1006` | <i lang="sa-Latn">√midṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ</i> |
| <a id="dhatu-01-1007"></a>`01.1007` | <i lang="sa-Latn">√medṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ saṅgame ca</i> |
| <a id="dhatu-01-1008"></a>`01.1008` | <i lang="sa-Latn">√mithṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ</i> |
| <a id="dhatu-01-1009"></a>`01.1009` | <i lang="sa-Latn">√methṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ</i> |
| <a id="dhatu-01-1010"></a>`01.1010` | <i lang="sa-Latn">√midhṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ</i> |
| <a id="dhatu-01-1011"></a>`01.1011` | <i lang="sa-Latn">√medhṛ~^</i> | <i lang="sa-Latn">medhāhiṃsanayoḥ saṅgame ca</i> |
| <a id="dhatu-01-1012"></a>`01.1012` | <i lang="sa-Latn">√ṇidṛ~^</i> | <i lang="sa-Latn">kutsāsannikarṣayoḥ</i> |
| <a id="dhatu-01-1013"></a>`01.1013` | <i lang="sa-Latn">√ṇedṛ~^</i> | <i lang="sa-Latn">kutsāsannikarṣayoḥ</i> |
| <a id="dhatu-01-1014"></a>`01.1014` | <i lang="sa-Latn">√śṛdhu~^</i> | <i lang="sa-Latn">undane</i> |
| <a id="dhatu-01-1015"></a>`01.1015` | <i lang="sa-Latn">√mṛdhu~^</i> | <i lang="sa-Latn">undane</i> |
| <a id="dhatu-01-1016"></a>`01.1016` | <i lang="sa-Latn">√budhi~^r</i> | <i lang="sa-Latn">bodhane</i> |
| <a id="dhatu-01-1017"></a>`01.1017` | <i lang="sa-Latn">√u~bundi~^r</i> | <i lang="sa-Latn">niśāmane</i> |
| <a id="dhatu-01-1018"></a>`01.1018` | <i lang="sa-Latn">√veṇṛ~^</i> | <i lang="sa-Latn">gatijñānacintāniśāmanavāditragrahaṇeṣu</i> |
| <a id="dhatu-01-1019"></a>`01.1019` | <i lang="sa-Latn">√venṛ~^</i> | <i lang="sa-Latn">gatijñānacintāniśāmanavāditragrahaṇeṣu</i> |
| <a id="dhatu-01-1020"></a>`01.1020` | <i lang="sa-Latn">√khanu~^</i> | <i lang="sa-Latn">avadāraṇe</i> |
| <a id="dhatu-01-1021"></a>`01.1021` | <i lang="sa-Latn">√cīvṛ~^</i> | <i lang="sa-Latn">ādānasaṃvaraṇayoḥ</i> |
| <a id="dhatu-01-1022"></a>`01.1022` | <i lang="sa-Latn">√cīpṛ~^</i> | <i lang="sa-Latn">ādānasaṃvaraṇayoḥ</i> |
| <a id="dhatu-01-1023"></a>`01.1023` | <i lang="sa-Latn">√cāyṛ~^</i> | <i lang="sa-Latn">pūjāniśāmanayoḥ</i> |
| <a id="dhatu-01-1024"></a>`01.1024` | <i lang="sa-Latn">√vyaya~^</i> | <i lang="sa-Latn">vittatyāge gatau ca</i> |
| <a id="dhatu-01-1025"></a>`01.1025` | <i lang="sa-Latn">√dāśṛ~^</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-01-1026"></a>`01.1026` | <i lang="sa-Latn">√bheṣṛ~^</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-01-1027"></a>`01.1027` | <i lang="sa-Latn">√bhreṣṛ~^</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1028"></a>`01.1028` | <i lang="sa-Latn">√bhleṣṛ~^</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1029"></a>`01.1029` | <i lang="sa-Latn">√asa~^</i> | <i lang="sa-Latn">gatidīptyādāneṣu</i> |
| <a id="dhatu-01-1030"></a>`01.1030` | <i lang="sa-Latn">√aṣa~^</i> | <i lang="sa-Latn">gatidīptyādāneṣu</i> |
| <a id="dhatu-01-1031"></a>`01.1031` | <i lang="sa-Latn">√ya\ma~</i> | <i lang="sa-Latn">uparame</i> |
| <a id="dhatu-01-1032"></a>`01.1032` | <i lang="sa-Latn">√spaśa~^</i> | <i lang="sa-Latn">bādhanasparśanayoḥ</i> |
| <a id="dhatu-01-1033"></a>`01.1033` | <i lang="sa-Latn">√laṣa~^</i> | <i lang="sa-Latn">kāntau</i> |
| <a id="dhatu-01-1034"></a>`01.1034` | <i lang="sa-Latn">√caṣa~^</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-01-1035"></a>`01.1035` | <i lang="sa-Latn">√chaṣa~^</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-01-1036"></a>`01.1036` | <i lang="sa-Latn">√jhaṣa~^</i> | <i lang="sa-Latn">ādānasaṃvaraṇayoḥ</i> |
| <a id="dhatu-01-1037"></a>`01.1037` | <i lang="sa-Latn">√bhrakṣa~^</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-1038"></a>`01.1038` | <i lang="sa-Latn">√bhlakṣa~^</i> | <i lang="sa-Latn">ādānasaṃvaraṇayoḥ</i> |
| <a id="dhatu-01-1039"></a>`01.1039` | <i lang="sa-Latn">√bhakṣa~^</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-1040"></a>`01.1040` | <i lang="sa-Latn">√plakṣa~^</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-01-1041"></a>`01.1041` | <i lang="sa-Latn">√dāsṛ~^</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-01-1042"></a>`01.1042` | <i lang="sa-Latn">√māhṛ~^</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-01-1043"></a>`01.1043` | <i lang="sa-Latn">√guhū~^</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-1044"></a>`01.1044` | <i lang="sa-Latn">√śriñ</i> | <i lang="sa-Latn">sevāyām</i> |
| <a id="dhatu-01-1045"></a>`01.1045` | <i lang="sa-Latn">√bhṛ\ñ</i> | <i lang="sa-Latn">bharaṇe</i> |
| <a id="dhatu-01-1046"></a>`01.1046` | <i lang="sa-Latn">√hṛ\ñ</i> | <i lang="sa-Latn">haraṇe</i> |
| <a id="dhatu-01-1047"></a>`01.1047` | <i lang="sa-Latn">√dhṛ\ñ</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-01-1048"></a>`01.1048` | <i lang="sa-Latn">√ṣūkṣya~</i> | <i lang="sa-Latn">īrṣyāyām</i> |
| <a id="dhatu-01-1049"></a>`01.1049` | <i lang="sa-Latn">√ṇī\ñ</i> | <i lang="sa-Latn">prāpaṇe</i> |
| <a id="dhatu-01-1050"></a>`01.1050` | <i lang="sa-Latn">√dhe\ṭ</i> | <i lang="sa-Latn">pāne</i> |
| <a id="dhatu-01-1051"></a>`01.1051` | <i lang="sa-Latn">√glai\</i> | <i lang="sa-Latn">harṣakṣaye</i> |
| <a id="dhatu-01-1052"></a>`01.1052` | <i lang="sa-Latn">√mlai\</i> | <i lang="sa-Latn">harṣakṣaye</i> |
| <a id="dhatu-01-1053"></a>`01.1053` | <i lang="sa-Latn">√dyai\</i> | <i lang="sa-Latn">nyakkaraṇe</i> |
| <a id="dhatu-01-1054"></a>`01.1054` | <i lang="sa-Latn">√drai\</i> | <i lang="sa-Latn">svapne</i> |
| <a id="dhatu-01-1055"></a>`01.1055` | <i lang="sa-Latn">√dhrai\</i> | <i lang="sa-Latn">tṛptau</i> |
| <a id="dhatu-01-1056"></a>`01.1056` | <i lang="sa-Latn">√dhyai\</i> | <i lang="sa-Latn">cintāyām</i> |
| <a id="dhatu-01-1057"></a>`01.1057` | <i lang="sa-Latn">√rai\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1058"></a>`01.1058` | <i lang="sa-Latn">√styai\</i> | <i lang="sa-Latn">śabdasaṅghātayoḥ</i> |
| <a id="dhatu-01-1059"></a>`01.1059` | <i lang="sa-Latn">√ṣṭyai\</i> | <i lang="sa-Latn">śabdasaṅghātayoḥ</i> |
| <a id="dhatu-01-1060"></a>`01.1060` | <i lang="sa-Latn">√khai\</i> | <i lang="sa-Latn">khadane</i> |
| <a id="dhatu-01-1061"></a>`01.1061` | <i lang="sa-Latn">√kṣai\</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-01-1062"></a>`01.1062` | <i lang="sa-Latn">√jai\</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-01-1063"></a>`01.1063` | <i lang="sa-Latn">√ṣai\</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-01-1064"></a>`01.1064` | <i lang="sa-Latn">√kai\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1065"></a>`01.1065` | <i lang="sa-Latn">√gai\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1066"></a>`01.1066` | <i lang="sa-Latn">√śai\</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-01-1067"></a>`01.1067` | <i lang="sa-Latn">√śrai\</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-01-1068"></a>`01.1068` | <i lang="sa-Latn">√srai\</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-01-1069"></a>`01.1069` | <i lang="sa-Latn">√pai\</i> | <i lang="sa-Latn">śoṣaṇe</i> |
| <a id="dhatu-01-1070"></a>`01.1070` | <i lang="sa-Latn">√o~vai\</i> | <i lang="sa-Latn">śoṣaṇe</i> |
| <a id="dhatu-01-1071"></a>`01.1071` | <i lang="sa-Latn">√ṣṭai\</i> | <i lang="sa-Latn">veṣṭane śobhāyāṃ ca</i> |
| <a id="dhatu-01-1072"></a>`01.1072` | <i lang="sa-Latn">√ṣṇai\</i> | <i lang="sa-Latn">veṣṭane śobhāyāṃ ca</i> |
| <a id="dhatu-01-1073"></a>`01.1073` | <i lang="sa-Latn">√dai\p</i> | <i lang="sa-Latn">śodhane</i> |
| <a id="dhatu-01-1074"></a>`01.1074` | <i lang="sa-Latn">√pā\</i> | <i lang="sa-Latn">pāne</i> |
| <a id="dhatu-01-1075"></a>`01.1075` | <i lang="sa-Latn">√ghrā\</i> | <i lang="sa-Latn">gandhopādāne ghrāṇe ca</i> |
| <a id="dhatu-01-1076"></a>`01.1076` | <i lang="sa-Latn">√dhmā\</i> | <i lang="sa-Latn">śabdāgnisaṃyogayoḥ</i> |
| <a id="dhatu-01-1077"></a>`01.1077` | <i lang="sa-Latn">√ṣṭhā\</i> | <i lang="sa-Latn">gatinivṛttau</i> |
| <a id="dhatu-01-1078"></a>`01.1078` | <i lang="sa-Latn">√mnā\</i> | <i lang="sa-Latn">abhyāse</i> |
| <a id="dhatu-01-1079"></a>`01.1079` | <i lang="sa-Latn">√dā\ṇ</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-01-1080"></a>`01.1080` | <i lang="sa-Latn">√hvṛ\</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-01-1081"></a>`01.1081` | <i lang="sa-Latn">√svṛ</i> | <i lang="sa-Latn">śabdopatāpayoḥ</i> |
| <a id="dhatu-01-1082"></a>`01.1082` | <i lang="sa-Latn">√smṛ\</i> | <i lang="sa-Latn">cintāyām</i> |
| <a id="dhatu-01-1083"></a>`01.1083` | <i lang="sa-Latn">√vṛ\</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-1084"></a>`01.1084` | <i lang="sa-Latn">√hvṛ\</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-1085"></a>`01.1085` | <i lang="sa-Latn">√sṛ\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1086"></a>`01.1086` | <i lang="sa-Latn">√ṛ\</i> | <i lang="sa-Latn">gatiprāpaṇayoḥ</i> |
| <a id="dhatu-01-1087"></a>`01.1087` | <i lang="sa-Latn">√gṛ\</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-1088"></a>`01.1088` | <i lang="sa-Latn">√ghṛ\</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-1089"></a>`01.1089` | <i lang="sa-Latn">√dhvṛ\</i> | <i lang="sa-Latn">hūrchane</i> |
| <a id="dhatu-01-1090"></a>`01.1090` | <i lang="sa-Latn">√sru\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1091"></a>`01.1091` | <i lang="sa-Latn">√ṣu\</i> | <i lang="sa-Latn">prasavaiśvaryayoḥ</i> |
| <a id="dhatu-01-1092"></a>`01.1092` | <i lang="sa-Latn">√śru\</i> | <i lang="sa-Latn">śravaṇe</i> |
| <a id="dhatu-01-1093"></a>`01.1093` | <i lang="sa-Latn">√dhru\</i> | <i lang="sa-Latn">sthairye</i> |
| <a id="dhatu-01-1094"></a>`01.1094` | <i lang="sa-Latn">√du\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1095"></a>`01.1095` | <i lang="sa-Latn">√dru\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1096"></a>`01.1096` | <i lang="sa-Latn">√ji\</i> | <i lang="sa-Latn">abhibhave (nyūnībhavane nyūnīkaraṇe ca)</i> |
| <a id="dhatu-01-1097"></a>`01.1097` | <i lang="sa-Latn">√jri\</i> | <i lang="sa-Latn">abhibhave (nyūnībhavane nyūnīkaraṇe ca)</i> |
| <a id="dhatu-01-1098"></a>`01.1098` | <i lang="sa-Latn">√jṛ\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1099"></a>`01.1099` | <i lang="sa-Latn">√ṣmi\ṅ</i> | <i lang="sa-Latn">īṣaddhasane</i> |
| <a id="dhatu-01-1100"></a>`01.1100` | <i lang="sa-Latn">√gu\ṅ</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-1101"></a>`01.1101` | <i lang="sa-Latn">√gā\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1102"></a>`01.1102` | <i lang="sa-Latn">√u\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1103"></a>`01.1103` | <i lang="sa-Latn">√ku\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1104"></a>`01.1104` | <i lang="sa-Latn">√khu\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1105"></a>`01.1105` | <i lang="sa-Latn">√gu\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1106"></a>`01.1106` | <i lang="sa-Latn">√ghu\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1107"></a>`01.1107` | <i lang="sa-Latn">√ṅu\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-01-1108"></a>`01.1108` | <i lang="sa-Latn">√cyu\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1109"></a>`01.1109` | <i lang="sa-Latn">√jyu\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1110"></a>`01.1110` | <i lang="sa-Latn">√chyu\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1111"></a>`01.1111` | <i lang="sa-Latn">√pru\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1112"></a>`01.1112` | <i lang="sa-Latn">√plu\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1113"></a>`01.1113` | <i lang="sa-Latn">√klu\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1114"></a>`01.1114` | <i lang="sa-Latn">√ru\ṅ</i> | <i lang="sa-Latn">gatiroṣaṇayoḥ</i> |
| <a id="dhatu-01-1115"></a>`01.1115` | <i lang="sa-Latn">√dhṛ\ṅ</i> | <i lang="sa-Latn">avabandhane vidhvaṃsane ca</i> |
| <a id="dhatu-01-1116"></a>`01.1116` | <i lang="sa-Latn">√me\ṅ</i> | <i lang="sa-Latn">praṇidāne</i> |
| <a id="dhatu-01-1117"></a>`01.1117` | <i lang="sa-Latn">√de\ṅ</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-01-1118"></a>`01.1118` | <i lang="sa-Latn">√śyai\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1119"></a>`01.1119` | <i lang="sa-Latn">√pyai\ṅ</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-01-1120"></a>`01.1120` | <i lang="sa-Latn">√trai\ṅ</i> | <i lang="sa-Latn">pālane</i> |
| <a id="dhatu-01-1121"></a>`01.1121` | <i lang="sa-Latn">√pūṅ</i> | <i lang="sa-Latn">pavane</i> |
| <a id="dhatu-01-1122"></a>`01.1122` | <i lang="sa-Latn">√mūṅ</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-01-1123"></a>`01.1123` | <i lang="sa-Latn">√ḍīṅ</i> | <i lang="sa-Latn">vihāyasā gatau</i> |
| <a id="dhatu-01-1124"></a>`01.1124` | <i lang="sa-Latn">√tṝ</i> | <i lang="sa-Latn">plavanataraṇayoḥ</i> |
| <a id="dhatu-01-1125"></a>`01.1125` | <i lang="sa-Latn">√gupa~\</i> | <i lang="sa-Latn">gopane nindāyāṃ ca</i> |
| <a id="dhatu-01-1126"></a>`01.1126` | <i lang="sa-Latn">√tija~\</i> | <i lang="sa-Latn">niśāne kṣamāyām ca</i> |
| <a id="dhatu-01-1127"></a>`01.1127` | <i lang="sa-Latn">√māna~\</i> | <i lang="sa-Latn">pūjāyām jijñāsāyāṃ ca</i> |
| <a id="dhatu-01-1128"></a>`01.1128` | <i lang="sa-Latn">√badha~\</i> | <i lang="sa-Latn">bandhane cittavikāre ca</i> |
| <a id="dhatu-01-1129"></a>`01.1129` | <i lang="sa-Latn">√ra\bha~\</i> | <i lang="sa-Latn">rābhasye</i> |
| <a id="dhatu-01-1130"></a>`01.1130` | <i lang="sa-Latn">√ḍula\bha~\ṣ</i> | <i lang="sa-Latn">prāptau</i> |
| <a id="dhatu-01-1131"></a>`01.1131` | <i lang="sa-Latn">√ṣva\nja~\</i> | <i lang="sa-Latn">pariṣvaṅge</i> |
| <a id="dhatu-01-1132"></a>`01.1132` | <i lang="sa-Latn">√ha\da~\</i> | <i lang="sa-Latn">purīṣotsarge</i> |
| <a id="dhatu-01-1133"></a>`01.1133` | <i lang="sa-Latn">√ñiṣvidā~</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-01-1134"></a>`01.1134` | <i lang="sa-Latn">√ska\ndi~r</i> | <i lang="sa-Latn">gatiśoṣaṇayoḥ</i> |
| <a id="dhatu-01-1135"></a>`01.1135` | <i lang="sa-Latn">√ya\bha~</i> | <i lang="sa-Latn">maithune</i> |
| <a id="dhatu-01-1136"></a>`01.1136` | <i lang="sa-Latn">√ṇa\ma~</i> | <i lang="sa-Latn">prahvatve śabde ca</i> |
| <a id="dhatu-01-1137"></a>`01.1137` | <i lang="sa-Latn">√ga\mḷ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1138"></a>`01.1138` | <i lang="sa-Latn">√sṛ\pḷ~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-01-1139"></a>`01.1139` | <i lang="sa-Latn">√ya\ma~</i> | <i lang="sa-Latn">uparame</i> |
| <a id="dhatu-01-1140"></a>`01.1140` | <i lang="sa-Latn">√ta\pa~</i> | <i lang="sa-Latn">santāpe</i> |
| <a id="dhatu-01-1141"></a>`01.1141` | <i lang="sa-Latn">√tya\ja~</i> | <i lang="sa-Latn">hānau</i> |
| <a id="dhatu-01-1142"></a>`01.1142` | <i lang="sa-Latn">√ṣa\nja~</i> | <i lang="sa-Latn">saṅge</i> |
| <a id="dhatu-01-1143"></a>`01.1143` | <i lang="sa-Latn">√dṛ\śi~r</i> | <i lang="sa-Latn">prekṣaṇe</i> |
| <a id="dhatu-01-1144"></a>`01.1144` | <i lang="sa-Latn">√da\nśa~</i> | <i lang="sa-Latn">daśane</i> |
| <a id="dhatu-01-1145"></a>`01.1145` | <i lang="sa-Latn">√kṛ\ṣa~</i> | <i lang="sa-Latn">vilekhane</i> |
| <a id="dhatu-01-1146"></a>`01.1146` | <i lang="sa-Latn">√da\ha~</i> | <i lang="sa-Latn">bhasmīkaraṇe</i> |
| <a id="dhatu-01-1147"></a>`01.1147` | <i lang="sa-Latn">√mi\ha~</i> | <i lang="sa-Latn">secane</i> |
| <a id="dhatu-01-1148"></a>`01.1148` | <i lang="sa-Latn">√kita~</i> | <i lang="sa-Latn">nivāse rogāpanayane vyādhipratīkāre nigrahe apanayane nāśane saṃśaye ca</i> |
| <a id="dhatu-01-1149"></a>`01.1149` | <i lang="sa-Latn">√dāna~^</i> | <i lang="sa-Latn">khaṇḍane ārjave ca</i> |
| <a id="dhatu-01-1150"></a>`01.1150` | <i lang="sa-Latn">√śāna~^</i> | <i lang="sa-Latn">tejane niśāne ca</i> |
| <a id="dhatu-01-1151"></a>`01.1151` | <i lang="sa-Latn">√ḍupa\ca~^ṣ</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-01-1152"></a>`01.1152` | <i lang="sa-Latn">√ṣaca~^</i> | <i lang="sa-Latn">samavāye</i> |
| <a id="dhatu-01-1153"></a>`01.1153` | <i lang="sa-Latn">√bha\ja~^</i> | <i lang="sa-Latn">sevāyām</i> |
| <a id="dhatu-01-1154"></a>`01.1154` | <i lang="sa-Latn">√ra\nja~^</i> | <i lang="sa-Latn">rāge</i> |
| <a id="dhatu-01-1155"></a>`01.1155` | <i lang="sa-Latn">√śa\pa~^</i> | <i lang="sa-Latn">ākrośe</i> |
| <a id="dhatu-01-1156"></a>`01.1156` | <i lang="sa-Latn">√tvi\ṣa~^</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-01-1157"></a>`01.1157` | <i lang="sa-Latn">√ya\ja~^</i> | <i lang="sa-Latn">devapūjāsaṅgatikaraṇadāneṣu</i> |
| <a id="dhatu-01-1158"></a>`01.1158` | <i lang="sa-Latn">√ḍuva\pa~^</i> | <i lang="sa-Latn">bījasantāne garbhādhāne chedane bījatantusantāne muṇḍabījoptyoḥ vapane gharṣaṇe tantunirmāṇe ca</i> |
| <a id="dhatu-01-1159"></a>`01.1159` | <i lang="sa-Latn">√va\ha~^</i> | <i lang="sa-Latn">prāpaṇe</i> |
| <a id="dhatu-01-1160"></a>`01.1160` | <i lang="sa-Latn">√va\sa~</i> | <i lang="sa-Latn">nivāse</i> |
| <a id="dhatu-01-1161"></a>`01.1161` | <i lang="sa-Latn">√ve\ñ</i> | <i lang="sa-Latn">tantusantāne</i> |
| <a id="dhatu-01-1162"></a>`01.1162` | <i lang="sa-Latn">√vye\ñ</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-01-1163"></a>`01.1163` | <i lang="sa-Latn">√hve\ñ</i> | <i lang="sa-Latn">spardhāyāṃ śabde ca</i> |
| <a id="dhatu-01-1164"></a>`01.1164` | <i lang="sa-Latn">√vada~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-01-1165"></a>`01.1165` | <i lang="sa-Latn">√ṭuo~śvi</i> | <i lang="sa-Latn">gativṛddhyoḥ</i> |
| <a id="dhatu-01-1166"></a>`01.1166` | <i lang="sa-Latn">√ṛti</i> | <i lang="sa-Latn">jugupsāyāṃ kṛpāyāṃ ca</i> |

<a id="gana-02"></a>
## Gaṇa 2 — <i lang="sa-Latn">adādi-gaṇaḥ</i> · <span lang="sa-Deva">अदादिगणः</span>

[Derivation chapter 2](#chapter-02) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-02-0001"></a>`02.0001` | <i lang="sa-Latn">√a\da~</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-02-0002"></a>`02.0002` | <i lang="sa-Latn">√ha\na~</i> | <i lang="sa-Latn">hiṃsāgatyoḥ</i> |
| <a id="dhatu-02-0003"></a>`02.0003` | <i lang="sa-Latn">√dvi\ṣa~^</i> | <i lang="sa-Latn">aprītau</i> |
| <a id="dhatu-02-0004"></a>`02.0004` | <i lang="sa-Latn">√du\ha~^</i> | <i lang="sa-Latn">prapūraṇe</i> |
| <a id="dhatu-02-0005"></a>`02.0005` | <i lang="sa-Latn">√di\ha~^</i> | <i lang="sa-Latn">upacaye</i> |
| <a id="dhatu-02-0006"></a>`02.0006` | <i lang="sa-Latn">√li\ha~^</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-02-0007"></a>`02.0007` | <i lang="sa-Latn">√ca\kṣi~\ṅ</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-02-0008"></a>`02.0008` | <i lang="sa-Latn">√īra~\</i> | <i lang="sa-Latn">gatau kampane ca</i> |
| <a id="dhatu-02-0009"></a>`02.0009` | <i lang="sa-Latn">√īḍa~\</i> | <i lang="sa-Latn">stutau</i> |
| <a id="dhatu-02-0010"></a>`02.0010` | <i lang="sa-Latn">√īśa~\</i> | <i lang="sa-Latn">aiśvarye</i> |
| <a id="dhatu-02-0011"></a>`02.0011` | <i lang="sa-Latn">√āsa~\</i> | <i lang="sa-Latn">upaveśane</i> |
| <a id="dhatu-02-0012"></a>`02.0012` | <i lang="sa-Latn">√śāsu~\</i> | <i lang="sa-Latn">icchāyām</i> |
| <a id="dhatu-02-0013"></a>`02.0013` | <i lang="sa-Latn">√vasa~\</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-02-0014"></a>`02.0014` | <i lang="sa-Latn">√kasi~\</i> | <i lang="sa-Latn">gatiśāsanayoḥ</i> |
| <a id="dhatu-02-0015"></a>`02.0015` | <i lang="sa-Latn">√kasa~\</i> | <i lang="sa-Latn">gatiśāsanayoḥ</i> |
| <a id="dhatu-02-0016"></a>`02.0016` | <i lang="sa-Latn">√kaśa~\</i> | <i lang="sa-Latn">gatiśāsanayoḥ</i> |
| <a id="dhatu-02-0017"></a>`02.0017` | <i lang="sa-Latn">√ṇisi~\</i> | <i lang="sa-Latn">cumbane</i> |
| <a id="dhatu-02-0018"></a>`02.0018` | <i lang="sa-Latn">√ṇiji~\</i> | <i lang="sa-Latn">śuddhau</i> |
| <a id="dhatu-02-0019"></a>`02.0019` | <i lang="sa-Latn">√śiji~\</i> | <i lang="sa-Latn">avyakte śabde</i> |
| <a id="dhatu-02-0020"></a>`02.0020` | <i lang="sa-Latn">√piji~\</i> | <i lang="sa-Latn">varṇe samparcane avayave avyakte śabde ca</i> |
| <a id="dhatu-02-0021"></a>`02.0021` | <i lang="sa-Latn">√pṛji~\</i> | <i lang="sa-Latn">varṇe</i> |
| <a id="dhatu-02-0022"></a>`02.0022` | <i lang="sa-Latn">√vṛjī~\</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-02-0023"></a>`02.0023` | <i lang="sa-Latn">√vṛji~\</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-02-0024"></a>`02.0024` | <i lang="sa-Latn">√pṛcī~\</i> | <i lang="sa-Latn">samparcane</i> |
| <a id="dhatu-02-0025"></a>`02.0025` | <i lang="sa-Latn">√ṣūṅ</i> | <i lang="sa-Latn">prāṇigarbhavimocane</i> |
| <a id="dhatu-02-0026"></a>`02.0026` | <i lang="sa-Latn">√śīṅ</i> | <i lang="sa-Latn">svapne</i> |
| <a id="dhatu-02-0027"></a>`02.0027` | <i lang="sa-Latn">√yu</i> | <i lang="sa-Latn">miśraṇe'miśraṇe ca</i> |
| <a id="dhatu-02-0028"></a>`02.0028` | <i lang="sa-Latn">√ru</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-02-0029"></a>`02.0029` | <i lang="sa-Latn">√tu\</i> | <i lang="sa-Latn">gativṛddhihiṃsāsu</i> |
| <a id="dhatu-02-0030"></a>`02.0030` | <i lang="sa-Latn">√ṇu</i> | <i lang="sa-Latn">stutau</i> |
| <a id="dhatu-02-0031"></a>`02.0031` | <i lang="sa-Latn">√ṭukṣu</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-02-0032"></a>`02.0032` | <i lang="sa-Latn">√kṣṇu</i> | <i lang="sa-Latn">tejane</i> |
| <a id="dhatu-02-0033"></a>`02.0033` | <i lang="sa-Latn">√ṣṇu</i> | <i lang="sa-Latn">prasravaṇe</i> |
| <a id="dhatu-02-0034"></a>`02.0034` | <i lang="sa-Latn">√ūrṇuñ</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-02-0035"></a>`02.0035` | <i lang="sa-Latn">√dyu\</i> | <i lang="sa-Latn">abhigamane</i> |
| <a id="dhatu-02-0036"></a>`02.0036` | <i lang="sa-Latn">√ṣu\</i> | <i lang="sa-Latn">prasavaiśvaryayoḥ</i> |
| <a id="dhatu-02-0037"></a>`02.0037` | <i lang="sa-Latn">√ku\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-02-0038"></a>`02.0038` | <i lang="sa-Latn">√ṣṭu\ñ</i> | <i lang="sa-Latn">stutau</i> |
| <a id="dhatu-02-0039"></a>`02.0039` | <i lang="sa-Latn">√brūñ</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-02-0040"></a>`02.0040` | <i lang="sa-Latn">√i\ṇ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-02-0041"></a>`02.0041` | <i lang="sa-Latn">√i\ṅ</i> | <i lang="sa-Latn">adhyayane</i> |
| <a id="dhatu-02-0042"></a>`02.0042` | <i lang="sa-Latn">√i\k</i> | <i lang="sa-Latn">smaraṇe</i> |
| <a id="dhatu-02-0043"></a>`02.0043` | <i lang="sa-Latn">√vī\</i> | <i lang="sa-Latn">gativyāptiprajanakāntyasanakhādaneṣu</i> |
| <a id="dhatu-02-0044"></a>`02.0044` | <i lang="sa-Latn">√yā\</i> | <i lang="sa-Latn">prāpaṇe</i> |
| <a id="dhatu-02-0045"></a>`02.0045` | <i lang="sa-Latn">√vā\</i> | <i lang="sa-Latn">gatigandhanayoḥ</i> |
| <a id="dhatu-02-0046"></a>`02.0046` | <i lang="sa-Latn">√bhā\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-02-0047"></a>`02.0047` | <i lang="sa-Latn">√ṣṇā\</i> | <i lang="sa-Latn">śauce</i> |
| <a id="dhatu-02-0048"></a>`02.0048` | <i lang="sa-Latn">√śrā\</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-02-0049"></a>`02.0049` | <i lang="sa-Latn">√drā\</i> | <i lang="sa-Latn">kutsāyāṃ gatau</i> |
| <a id="dhatu-02-0050"></a>`02.0050` | <i lang="sa-Latn">√psā\</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-02-0051"></a>`02.0051` | <i lang="sa-Latn">√pā\</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-02-0052"></a>`02.0052` | <i lang="sa-Latn">√rā\</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-02-0053"></a>`02.0053` | <i lang="sa-Latn">√lā\</i> | <i lang="sa-Latn">ādāne</i> |
| <a id="dhatu-02-0054"></a>`02.0054` | <i lang="sa-Latn">√dā\p</i> | <i lang="sa-Latn">lavane</i> |
| <a id="dhatu-02-0055"></a>`02.0055` | <i lang="sa-Latn">√khyā\</i> | <i lang="sa-Latn">prakathane</i> |
| <a id="dhatu-02-0056"></a>`02.0056` | <i lang="sa-Latn">√prā\</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-02-0057"></a>`02.0057` | <i lang="sa-Latn">√mā\</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-02-0058"></a>`02.0058` | <i lang="sa-Latn">√va\ca~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-02-0059"></a>`02.0059` | <i lang="sa-Latn">√vida~</i> | <i lang="sa-Latn">jñāne</i> |
| <a id="dhatu-02-0060"></a>`02.0060` | <i lang="sa-Latn">√asa~</i> | <i lang="sa-Latn">bhuvi</i> |
| <a id="dhatu-02-0061"></a>`02.0061` | <i lang="sa-Latn">√mṛjū~</i> | <i lang="sa-Latn">śuddhau</i> |
| <a id="dhatu-02-0062"></a>`02.0062` | <i lang="sa-Latn">√rudi~r</i> | <i lang="sa-Latn">aśruvimocane</i> |
| <a id="dhatu-02-0063"></a>`02.0063` | <i lang="sa-Latn">√ñiṣva\pa~</i> | <i lang="sa-Latn">śaye</i> |
| <a id="dhatu-02-0064"></a>`02.0064` | <i lang="sa-Latn">√śvasa~</i> | <i lang="sa-Latn">prāṇane</i> |
| <a id="dhatu-02-0065"></a>`02.0065` | <i lang="sa-Latn">√ana~</i> | <i lang="sa-Latn">prāṇane</i> |
| <a id="dhatu-02-0066"></a>`02.0066` | <i lang="sa-Latn">√jakṣa~</i> | <i lang="sa-Latn">bhakṣahasanayoḥ</i> |
| <a id="dhatu-02-0067"></a>`02.0067` | <i lang="sa-Latn">√jāgṛ</i> | <i lang="sa-Latn">nidrākṣaye</i> |
| <a id="dhatu-02-0068"></a>`02.0068` | <i lang="sa-Latn">√daridrā</i> | <i lang="sa-Latn">durgatau</i> |
| <a id="dhatu-02-0069"></a>`02.0069` | <i lang="sa-Latn">√cakāsṛ~</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-02-0070"></a>`02.0070` | <i lang="sa-Latn">√śāsu~</i> | <i lang="sa-Latn">anuśiṣṭau</i> |
| <a id="dhatu-02-0071"></a>`02.0071` | <i lang="sa-Latn">√dīdhīṅ</i> | <i lang="sa-Latn">dīptidevanayoḥ</i> |
| <a id="dhatu-02-0072"></a>`02.0072` | <i lang="sa-Latn">√vevīṅ</i> | <i lang="sa-Latn">gativyāptiprajanakāntyasanasvādaneṣu</i> |
| <a id="dhatu-02-0073"></a>`02.0073` | <i lang="sa-Latn">√ṣasa~</i> | <i lang="sa-Latn">svapne</i> |
| <a id="dhatu-02-0074"></a>`02.0074` | <i lang="sa-Latn">√ṣasti~</i> | <i lang="sa-Latn">svapne</i> |
| <a id="dhatu-02-0075"></a>`02.0075` | <i lang="sa-Latn">√vaśa~</i> | <i lang="sa-Latn">kāntau</i> |
| <a id="dhatu-02-0077"></a>`02.0077` | <i lang="sa-Latn">√hnu\ṅ</i> | <i lang="sa-Latn">apanayane</i> |

<a id="gana-03"></a>
## Gaṇa 3 — <i lang="sa-Latn">juhotyādi-gaṇaḥ</i> · <span lang="sa-Deva">जुहोत्यादिगणः</span>

[Derivation chapter 3](#chapter-03) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-03-0001"></a>`03.0001` | <i lang="sa-Latn">√hu\</i> | <i lang="sa-Latn">dānādānayoḥ ādāne prīṇane ca</i> |
| <a id="dhatu-03-0002"></a>`03.0002` | <i lang="sa-Latn">√ñibhī\</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-03-0003"></a>`03.0003` | <i lang="sa-Latn">√hrī\</i> | <i lang="sa-Latn">lajjāyām</i> |
| <a id="dhatu-03-0004"></a>`03.0004` | <i lang="sa-Latn">√pṝ</i> | <i lang="sa-Latn">pālanapūraṇayoḥ</i> |
| <a id="dhatu-03-0005"></a>`03.0005` | <i lang="sa-Latn">√pṛ\</i> | <i lang="sa-Latn">pālanapūraṇayoḥ</i> |
| <a id="dhatu-03-0006"></a>`03.0006` | <i lang="sa-Latn">√ḍubhṛ\ñ</i> | <i lang="sa-Latn">dhāraṇapoṣaṇayoḥ</i> |
| <a id="dhatu-03-0007"></a>`03.0007` | <i lang="sa-Latn">√mā\ṅ</i> | <i lang="sa-Latn">māne śabde ca</i> |
| <a id="dhatu-03-0008"></a>`03.0008` | <i lang="sa-Latn">√o~hā\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-03-0009"></a>`03.0009` | <i lang="sa-Latn">√o~hā\k</i> | <i lang="sa-Latn">tyāge</i> |
| <a id="dhatu-03-0010"></a>`03.0010` | <i lang="sa-Latn">√ḍudā\ñ</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-03-0011"></a>`03.0011` | <i lang="sa-Latn">√ḍudhā\ñ</i> | <i lang="sa-Latn">dhāraṇapoṣaṇayoḥ</i> |
| <a id="dhatu-03-0012"></a>`03.0012` | <i lang="sa-Latn">√ṇi\ji~^r</i> | <i lang="sa-Latn">śaucapoṣaṇayoḥ</i> |
| <a id="dhatu-03-0013"></a>`03.0013` | <i lang="sa-Latn">√vi\ji~^r</i> | <i lang="sa-Latn">pṛthagbhāve</i> |
| <a id="dhatu-03-0014"></a>`03.0014` | <i lang="sa-Latn">√vi\ṣḷ~^</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-03-0015"></a>`03.0015` | <i lang="sa-Latn">√ghṛ\</i> | <i lang="sa-Latn">kṣaraṇadīptyoḥ</i> |
| <a id="dhatu-03-0016"></a>`03.0016` | <i lang="sa-Latn">√hṛ\</i> | <i lang="sa-Latn">prasahyakaraṇe</i> |
| <a id="dhatu-03-0017"></a>`03.0017` | <i lang="sa-Latn">√ṛ\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-03-0018"></a>`03.0018` | <i lang="sa-Latn">√sṛ\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-03-0019"></a>`03.0019` | <i lang="sa-Latn">√bhasa~</i> | <i lang="sa-Latn">bhartsanadīptyoḥ</i> |
| <a id="dhatu-03-0020"></a>`03.0020` | <i lang="sa-Latn">√ki\</i> | <i lang="sa-Latn">jñāne</i> |
| <a id="dhatu-03-0021"></a>`03.0021` | <i lang="sa-Latn">√kita~</i> | <i lang="sa-Latn">jñāne</i> |
| <a id="dhatu-03-0022"></a>`03.0022` | <i lang="sa-Latn">√tura~</i> | <i lang="sa-Latn">tvaraṇe</i> |
| <a id="dhatu-03-0023"></a>`03.0023` | <i lang="sa-Latn">√dhiṣa~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-03-0024"></a>`03.0024` | <i lang="sa-Latn">√dhana~</i> | <i lang="sa-Latn">dhānye</i> |
| <a id="dhatu-03-0025"></a>`03.0025` | <i lang="sa-Latn">√jana~</i> | <i lang="sa-Latn">janane</i> |
| <a id="dhatu-03-0026"></a>`03.0026` | <i lang="sa-Latn">√gā\</i> | <i lang="sa-Latn">stutau</i> |

<a id="gana-04"></a>
## Gaṇa 4 — <i lang="sa-Latn">divādi-gaṇaḥ</i> · <span lang="sa-Deva">दिवादिगणः</span>

[Derivation chapter 4](#chapter-04) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-04-0001"></a>`04.0001` | <i lang="sa-Latn">√divu~</i> | <i lang="sa-Latn">krīḍāvijigīṣāvyavahāradyutistutimodamadasvapnakāntigatiṣu</i> |
| <a id="dhatu-04-0002"></a>`04.0002` | <i lang="sa-Latn">√ṣivu~</i> | <i lang="sa-Latn">tantusantāne</i> |
| <a id="dhatu-04-0003"></a>`04.0003` | <i lang="sa-Latn">√srivu~</i> | <i lang="sa-Latn">gatiśoṣaṇayoḥ</i> |
| <a id="dhatu-04-0004"></a>`04.0004` | <i lang="sa-Latn">√ṣṭhivu~</i> | <i lang="sa-Latn">nirasane</i> |
| <a id="dhatu-04-0005"></a>`04.0005` | <i lang="sa-Latn">√ṣṇusu~</i> | <i lang="sa-Latn">adane ādāne adarśane ca</i> |
| <a id="dhatu-04-0006"></a>`04.0006` | <i lang="sa-Latn">√ṣṇasu~</i> | <i lang="sa-Latn">adane nirasane ca</i> |
| <a id="dhatu-04-0007"></a>`04.0007` | <i lang="sa-Latn">√knasu~</i> | <i lang="sa-Latn">hvaraṇadīptyoḥ</i> |
| <a id="dhatu-04-0008"></a>`04.0008` | <i lang="sa-Latn">√vyuṣa~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-04-0009"></a>`04.0009` | <i lang="sa-Latn">√pluṣa~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-04-0010"></a>`04.0010` | <i lang="sa-Latn">√nṛtī~</i> | <i lang="sa-Latn">gātravikṣepe</i> |
| <a id="dhatu-04-0011"></a>`04.0011` | <i lang="sa-Latn">√trasī~</i> | <i lang="sa-Latn">udvege</i> |
| <a id="dhatu-04-0012"></a>`04.0012` | <i lang="sa-Latn">√kutha~</i> | <i lang="sa-Latn">pūtībhāve</i> |
| <a id="dhatu-04-0013"></a>`04.0013` | <i lang="sa-Latn">√putha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0014"></a>`04.0014` | <i lang="sa-Latn">√gudha~</i> | <i lang="sa-Latn">pariveṣṭane</i> |
| <a id="dhatu-04-0015"></a>`04.0015` | <i lang="sa-Latn">√kṣi\pa~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-04-0016"></a>`04.0016` | <i lang="sa-Latn">√puṣpa~</i> | <i lang="sa-Latn">vikasane</i> |
| <a id="dhatu-04-0017"></a>`04.0017` | <i lang="sa-Latn">√tima~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0018"></a>`04.0018` | <i lang="sa-Latn">√tīma~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0019"></a>`04.0019` | <i lang="sa-Latn">√ṣṭima~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0020"></a>`04.0020` | <i lang="sa-Latn">√ṣṭīma~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0021"></a>`04.0021` | <i lang="sa-Latn">√vrīḍa~</i> | <i lang="sa-Latn">codane lajjāyāṃ ca</i> |
| <a id="dhatu-04-0022"></a>`04.0022` | <i lang="sa-Latn">√iṣa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-04-0023"></a>`04.0023` | <i lang="sa-Latn">√ṣaha~</i> | <i lang="sa-Latn">cakyarthe</i> |
| <a id="dhatu-04-0024"></a>`04.0024` | <i lang="sa-Latn">√ṣuha~</i> | <i lang="sa-Latn">cakyarthe</i> |
| <a id="dhatu-04-0025"></a>`04.0025` | <i lang="sa-Latn">√jṝṣ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-04-0026"></a>`04.0026` | <i lang="sa-Latn">√jhṝṣ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-04-0027"></a>`04.0027` | <i lang="sa-Latn">√ṣūṅ</i> | <i lang="sa-Latn">prāṇiprasave</i> |
| <a id="dhatu-04-0028"></a>`04.0028` | <i lang="sa-Latn">√dūṅ</i> | <i lang="sa-Latn">paritāpe</i> |
| <a id="dhatu-04-0029"></a>`04.0029` | <i lang="sa-Latn">√dī\ṅ</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-04-0030"></a>`04.0030` | <i lang="sa-Latn">√ḍīṅ</i> | <i lang="sa-Latn">vihāyasā gatau</i> |
| <a id="dhatu-04-0031"></a>`04.0031` | <i lang="sa-Latn">√dhī\ṅ</i> | <i lang="sa-Latn">ādhāre ādāne anādare ca</i> |
| <a id="dhatu-04-0032"></a>`04.0032` | <i lang="sa-Latn">√mī\ṅ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0033"></a>`04.0033` | <i lang="sa-Latn">√rī\ṅ</i> | <i lang="sa-Latn">sravaṇe</i> |
| <a id="dhatu-04-0034"></a>`04.0034` | <i lang="sa-Latn">√lī\ṅ</i> | <i lang="sa-Latn">śleṣaṇe</i> |
| <a id="dhatu-04-0035"></a>`04.0035` | <i lang="sa-Latn">√vrī\ṅ</i> | <i lang="sa-Latn">vṛṇotyarthe</i> |
| <a id="dhatu-04-0036"></a>`04.0036` | <i lang="sa-Latn">√pī\ṅ</i> | <i lang="sa-Latn">pāne</i> |
| <a id="dhatu-04-0037"></a>`04.0037` | <i lang="sa-Latn">√mā\ṅ</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-04-0038"></a>`04.0038` | <i lang="sa-Latn">√ī\ṅ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-04-0039"></a>`04.0039` | <i lang="sa-Latn">√prī\ṅ</i> | <i lang="sa-Latn">prītau</i> |
| <a id="dhatu-04-0040"></a>`04.0040` | <i lang="sa-Latn">√śo\</i> | <i lang="sa-Latn">tanūkaraṇe</i> |
| <a id="dhatu-04-0041"></a>`04.0041` | <i lang="sa-Latn">√cho\</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-04-0042"></a>`04.0042` | <i lang="sa-Latn">√ṣo\</i> | <i lang="sa-Latn">antakarmaṇi</i> |
| <a id="dhatu-04-0043"></a>`04.0043` | <i lang="sa-Latn">√do\</i> | <i lang="sa-Latn">avakhaṇḍane</i> |
| <a id="dhatu-04-0044"></a>`04.0044` | <i lang="sa-Latn">√janī~\</i> | <i lang="sa-Latn">prādurbhāve</i> |
| <a id="dhatu-04-0045"></a>`04.0045` | <i lang="sa-Latn">√dīpī~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-04-0046"></a>`04.0046` | <i lang="sa-Latn">√pūrī~\</i> | <i lang="sa-Latn">āpyāyane</i> |
| <a id="dhatu-04-0047"></a>`04.0047` | <i lang="sa-Latn">√tūrī~\</i> | <i lang="sa-Latn">gatitvaraṇahiṃsanayoḥ</i> |
| <a id="dhatu-04-0048"></a>`04.0048` | <i lang="sa-Latn">√dhūrī~\</i> | <i lang="sa-Latn">hiṃsāgatyoḥ</i> |
| <a id="dhatu-04-0049"></a>`04.0049` | <i lang="sa-Latn">√gūrī~\</i> | <i lang="sa-Latn">hiṃsāgatyoḥ</i> |
| <a id="dhatu-04-0050"></a>`04.0050` | <i lang="sa-Latn">√ghūrī~\</i> | <i lang="sa-Latn">hiṃsāvayohānyoḥ</i> |
| <a id="dhatu-04-0051"></a>`04.0051` | <i lang="sa-Latn">√jūrī~\</i> | <i lang="sa-Latn">hiṃsāvayohānyoḥ</i> |
| <a id="dhatu-04-0052"></a>`04.0052` | <i lang="sa-Latn">√śūrī~\</i> | <i lang="sa-Latn">hiṃsāstambhanayoḥ</i> |
| <a id="dhatu-04-0053"></a>`04.0053` | <i lang="sa-Latn">√cūrī~\</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-04-0054"></a>`04.0054` | <i lang="sa-Latn">√ta\pa~\</i> | <i lang="sa-Latn">aiśvarye</i> |
| <a id="dhatu-04-0055"></a>`04.0055` | <i lang="sa-Latn">√vṛtu~\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-04-0056"></a>`04.0056` | <i lang="sa-Latn">√vāvṛtu~\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-04-0057"></a>`04.0057` | <i lang="sa-Latn">√kliśa~\</i> | <i lang="sa-Latn">upatāpe</i> |
| <a id="dhatu-04-0058"></a>`04.0058` | <i lang="sa-Latn">√kāśṛ~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-04-0059"></a>`04.0059` | <i lang="sa-Latn">√vāśṛ~\</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-04-0060"></a>`04.0060` | <i lang="sa-Latn">√mṛṣa~^</i> | <i lang="sa-Latn">titikṣāyām</i> |
| <a id="dhatu-04-0061"></a>`04.0061` | <i lang="sa-Latn">√ī~śuci~^r</i> | <i lang="sa-Latn">pūtībhāve</i> |
| <a id="dhatu-04-0062"></a>`04.0062` | <i lang="sa-Latn">√ṇa\ha~^</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-04-0063"></a>`04.0063` | <i lang="sa-Latn">√ra\nja~^</i> | <i lang="sa-Latn">rāge</i> |
| <a id="dhatu-04-0064"></a>`04.0064` | <i lang="sa-Latn">√śa\pa~^</i> | <i lang="sa-Latn">ākrośe</i> |
| <a id="dhatu-04-0065"></a>`04.0065` | <i lang="sa-Latn">√pa\da~\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-04-0066"></a>`04.0066` | <i lang="sa-Latn">√khi\da~\</i> | <i lang="sa-Latn">dainye</i> |
| <a id="dhatu-04-0067"></a>`04.0067` | <i lang="sa-Latn">√vi\da~\</i> | <i lang="sa-Latn">sattāyām</i> |
| <a id="dhatu-04-0068"></a>`04.0068` | <i lang="sa-Latn">√bu\dha~\</i> | <i lang="sa-Latn">avagamane</i> |
| <a id="dhatu-04-0069"></a>`04.0069` | <i lang="sa-Latn">√yu\dha~\</i> | <i lang="sa-Latn">samprahāre</i> |
| <a id="dhatu-04-0070"></a>`04.0070` | <i lang="sa-Latn">√ru\dha~\</i> | <i lang="sa-Latn">kāme</i> |
| <a id="dhatu-04-0071"></a>`04.0071` | <i lang="sa-Latn">√aṇa~\</i> | <i lang="sa-Latn">prāṇane</i> |
| <a id="dhatu-04-0072"></a>`04.0072` | <i lang="sa-Latn">√ana~\</i> | <i lang="sa-Latn">prāṇane</i> |
| <a id="dhatu-04-0073"></a>`04.0073` | <i lang="sa-Latn">√ma\na~\</i> | <i lang="sa-Latn">jñāne</i> |
| <a id="dhatu-04-0074"></a>`04.0074` | <i lang="sa-Latn">√yu\ja~\</i> | <i lang="sa-Latn">samādhau</i> |
| <a id="dhatu-04-0075"></a>`04.0075` | <i lang="sa-Latn">√sṛ\ja~\</i> | <i lang="sa-Latn">visarge</i> |
| <a id="dhatu-04-0076"></a>`04.0076` | <i lang="sa-Latn">√li\śa~\</i> | <i lang="sa-Latn">alpībhāve</i> |
| <a id="dhatu-04-0077"></a>`04.0077` | <i lang="sa-Latn">√rā\dha~</i> | <i lang="sa-Latn">vṛddhisiddhidrohadaivaparyālocanādiṣu ca</i> |
| <a id="dhatu-04-0078"></a>`04.0078` | <i lang="sa-Latn">√vya\dha~</i> | <i lang="sa-Latn">tāḍane</i> |
| <a id="dhatu-04-0079"></a>`04.0079` | <i lang="sa-Latn">√pu\ṣa~</i> | <i lang="sa-Latn">puṣṭau</i> |
| <a id="dhatu-04-0080"></a>`04.0080` | <i lang="sa-Latn">√śu\ṣa~</i> | <i lang="sa-Latn">śoṣaṇe</i> |
| <a id="dhatu-04-0081"></a>`04.0081` | <i lang="sa-Latn">√tu\ṣa~</i> | <i lang="sa-Latn">prītau</i> |
| <a id="dhatu-04-0082"></a>`04.0082` | <i lang="sa-Latn">√du\ṣa~</i> | <i lang="sa-Latn">vaikṛtye</i> |
| <a id="dhatu-04-0083"></a>`04.0083` | <i lang="sa-Latn">√śli\ṣa~</i> | <i lang="sa-Latn">āliṅgane</i> |
| <a id="dhatu-04-0084"></a>`04.0084` | <i lang="sa-Latn">√śa\ka~^</i> | <i lang="sa-Latn">marṣaṇe</i> |
| <a id="dhatu-04-0085"></a>`04.0085` | <i lang="sa-Latn">√ṣvi\dā~</i> | <i lang="sa-Latn">gātraprakṣaraṇe</i> |
| <a id="dhatu-04-0086"></a>`04.0086` | <i lang="sa-Latn">√kru\dha~</i> | <i lang="sa-Latn">krodhe</i> |
| <a id="dhatu-04-0087"></a>`04.0087` | <i lang="sa-Latn">√kṣu\dha~</i> | <i lang="sa-Latn">bubhukṣāyām</i> |
| <a id="dhatu-04-0088"></a>`04.0088` | <i lang="sa-Latn">√śu\dha~</i> | <i lang="sa-Latn">śauce</i> |
| <a id="dhatu-04-0089"></a>`04.0089` | <i lang="sa-Latn">√ṣi\dhu~</i> | <i lang="sa-Latn">saṃrāddhau</i> |
| <a id="dhatu-04-0090"></a>`04.0090` | <i lang="sa-Latn">√ra\dha~</i> | <i lang="sa-Latn">hiṃsāsaṃrāddhyoḥ</i> |
| <a id="dhatu-04-0091"></a>`04.0091` | <i lang="sa-Latn">√ṇa\śa~</i> | <i lang="sa-Latn">adarśane</i> |
| <a id="dhatu-04-0092"></a>`04.0092` | <i lang="sa-Latn">√tṛ\pa~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-04-0093"></a>`04.0093` | <i lang="sa-Latn">√dṛ\pa~</i> | <i lang="sa-Latn">harṣamohanayoḥ</i> |
| <a id="dhatu-04-0094"></a>`04.0094` | <i lang="sa-Latn">√dru\ha~</i> | <i lang="sa-Latn">jighāṃsāyām</i> |
| <a id="dhatu-04-0095"></a>`04.0095` | <i lang="sa-Latn">√mu\ha~</i> | <i lang="sa-Latn">vaicittye</i> |
| <a id="dhatu-04-0096"></a>`04.0096` | <i lang="sa-Latn">√ṣṇu\ha~</i> | <i lang="sa-Latn">udgiraṇe</i> |
| <a id="dhatu-04-0097"></a>`04.0097` | <i lang="sa-Latn">√ṣṇi\ha~</i> | <i lang="sa-Latn">prītau</i> |
| <a id="dhatu-04-0098"></a>`04.0098` | <i lang="sa-Latn">√śamu~</i> | <i lang="sa-Latn">upaśame</i> |
| <a id="dhatu-04-0099"></a>`04.0099` | <i lang="sa-Latn">√tamu~</i> | <i lang="sa-Latn">kāṅkṣāyām</i> |
| <a id="dhatu-04-0100"></a>`04.0100` | <i lang="sa-Latn">√damu~</i> | <i lang="sa-Latn">upaśame</i> |
| <a id="dhatu-04-0101"></a>`04.0101` | <i lang="sa-Latn">√śramu~</i> | <i lang="sa-Latn">tapasi khede ca</i> |
| <a id="dhatu-04-0102"></a>`04.0102` | <i lang="sa-Latn">√bhramu~</i> | <i lang="sa-Latn">anavasthāne</i> |
| <a id="dhatu-04-0103"></a>`04.0103` | <i lang="sa-Latn">√kṣamū~</i> | <i lang="sa-Latn">sahane</i> |
| <a id="dhatu-04-0104"></a>`04.0104` | <i lang="sa-Latn">√klamu~</i> | <i lang="sa-Latn">glānau</i> |
| <a id="dhatu-04-0105"></a>`04.0105` | <i lang="sa-Latn">√madī~</i> | <i lang="sa-Latn">harṣe glepane ca</i> |
| <a id="dhatu-04-0106"></a>`04.0106` | <i lang="sa-Latn">√asu~</i> | <i lang="sa-Latn">kṣepaṇe</i> |
| <a id="dhatu-04-0107"></a>`04.0107` | <i lang="sa-Latn">√yasu~</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-04-0108"></a>`04.0108` | <i lang="sa-Latn">√jasu~</i> | <i lang="sa-Latn">mokṣaṇe</i> |
| <a id="dhatu-04-0109"></a>`04.0109` | <i lang="sa-Latn">√tasu~</i> | <i lang="sa-Latn">upakṣaye</i> |
| <a id="dhatu-04-0110"></a>`04.0110` | <i lang="sa-Latn">√dasu~</i> | <i lang="sa-Latn">upakṣaye</i> |
| <a id="dhatu-04-0111"></a>`04.0111` | <i lang="sa-Latn">√vasu~</i> | <i lang="sa-Latn">stambhe</i> |
| <a id="dhatu-04-0112"></a>`04.0112` | <i lang="sa-Latn">√basu~</i> | <i lang="sa-Latn">stambhe</i> |
| <a id="dhatu-04-0113"></a>`04.0113` | <i lang="sa-Latn">√yusa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0114"></a>`04.0114` | <i lang="sa-Latn">√vyuṣa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0115"></a>`04.0115` | <i lang="sa-Latn">√vyusa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0116"></a>`04.0116` | <i lang="sa-Latn">√byusa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0117"></a>`04.0117` | <i lang="sa-Latn">√busa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0118"></a>`04.0118` | <i lang="sa-Latn">√vusa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0119"></a>`04.0119` | <i lang="sa-Latn">√pyuṣa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0120"></a>`04.0120` | <i lang="sa-Latn">√pyusa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0121"></a>`04.0121` | <i lang="sa-Latn">√puṣa~</i> | <i lang="sa-Latn">vibhāge</i> |
| <a id="dhatu-04-0122"></a>`04.0122` | <i lang="sa-Latn">√pluṣa~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-04-0123"></a>`04.0123` | <i lang="sa-Latn">√visa~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-04-0124"></a>`04.0124` | <i lang="sa-Latn">√bisa~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-04-0125"></a>`04.0125` | <i lang="sa-Latn">√kusa~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-04-0126"></a>`04.0126` | <i lang="sa-Latn">√kuśa~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-04-0127"></a>`04.0127` | <i lang="sa-Latn">√ñiṣvidā~</i> | <i lang="sa-Latn">gātraprakṣaraṇe</i> |
| <a id="dhatu-04-0128"></a>`04.0128` | <i lang="sa-Latn">√kṣamū~ṣ</i> | <i lang="sa-Latn">sahane</i> |
| <a id="dhatu-04-0129"></a>`04.0129` | <i lang="sa-Latn">√busa~</i> | <i lang="sa-Latn">utsarge</i> |
| <a id="dhatu-04-0130"></a>`04.0130` | <i lang="sa-Latn">√musa~</i> | <i lang="sa-Latn">khaṇḍane</i> |
| <a id="dhatu-04-0131"></a>`04.0131` | <i lang="sa-Latn">√masī~</i> | <i lang="sa-Latn">pariṇāme</i> |
| <a id="dhatu-04-0132"></a>`04.0132` | <i lang="sa-Latn">√samī~</i> | <i lang="sa-Latn">pariṇāme</i> |
| <a id="dhatu-04-0133"></a>`04.0133` | <i lang="sa-Latn">√luṭa~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-04-0134"></a>`04.0134` | <i lang="sa-Latn">√luṭha~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-04-0135"></a>`04.0135` | <i lang="sa-Latn">√uca~</i> | <i lang="sa-Latn">samavāye</i> |
| <a id="dhatu-04-0136"></a>`04.0136` | <i lang="sa-Latn">√bhṛśu~</i> | <i lang="sa-Latn">adhaḥpatane</i> |
| <a id="dhatu-04-0137"></a>`04.0137` | <i lang="sa-Latn">√stima~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0138"></a>`04.0138` | <i lang="sa-Latn">√bhranśu~</i> | <i lang="sa-Latn">adhaḥpatane</i> |
| <a id="dhatu-04-0139"></a>`04.0139` | <i lang="sa-Latn">√vṛśa~</i> | <i lang="sa-Latn">āvaraṇe</i> |
| <a id="dhatu-04-0140"></a>`04.0140` | <i lang="sa-Latn">√kṛśa~</i> | <i lang="sa-Latn">tanūkaraṇe</i> |
| <a id="dhatu-04-0141"></a>`04.0141` | <i lang="sa-Latn">√ñitṛṣā~</i> | <i lang="sa-Latn">pipāsāyām</i> |
| <a id="dhatu-04-0142"></a>`04.0142` | <i lang="sa-Latn">√hṛṣa~</i> | <i lang="sa-Latn">tuṣṭau</i> |
| <a id="dhatu-04-0143"></a>`04.0143` | <i lang="sa-Latn">√ruṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0144"></a>`04.0144` | <i lang="sa-Latn">√riṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0145"></a>`04.0145` | <i lang="sa-Latn">√ḍipa~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-04-0146"></a>`04.0146` | <i lang="sa-Latn">√kupa~</i> | <i lang="sa-Latn">krodhe</i> |
| <a id="dhatu-04-0147"></a>`04.0147` | <i lang="sa-Latn">√gupa~</i> | <i lang="sa-Latn">vyākulatve</i> |
| <a id="dhatu-04-0148"></a>`04.0148` | <i lang="sa-Latn">√yupa~</i> | <i lang="sa-Latn">vimohane</i> |
| <a id="dhatu-04-0149"></a>`04.0149` | <i lang="sa-Latn">√rupa~</i> | <i lang="sa-Latn">vimohane</i> |
| <a id="dhatu-04-0150"></a>`04.0150` | <i lang="sa-Latn">√lupa~</i> | <i lang="sa-Latn">vimohane</i> |
| <a id="dhatu-04-0151"></a>`04.0151` | <i lang="sa-Latn">√ṣṭupa~</i> | <i lang="sa-Latn">samucchrāye</i> |
| <a id="dhatu-04-0152"></a>`04.0152` | <i lang="sa-Latn">√ṣṭūpa~</i> | <i lang="sa-Latn">samucchrāye</i> |
| <a id="dhatu-04-0153"></a>`04.0153` | <i lang="sa-Latn">√lubha~</i> | <i lang="sa-Latn">gārddhye</i> |
| <a id="dhatu-04-0154"></a>`04.0154` | <i lang="sa-Latn">√kṣubha~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-04-0155"></a>`04.0155` | <i lang="sa-Latn">√ṇabha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0156"></a>`04.0156` | <i lang="sa-Latn">√tubha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-04-0157"></a>`04.0157` | <i lang="sa-Latn">√klidū~</i> | <i lang="sa-Latn">ārdrībhāve</i> |
| <a id="dhatu-04-0158"></a>`04.0158` | <i lang="sa-Latn">√ñimidā~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-04-0159"></a>`04.0159` | <i lang="sa-Latn">√ñikṣvidā~</i> | <i lang="sa-Latn">snehanamocanayoḥ</i> |
| <a id="dhatu-04-0160"></a>`04.0160` | <i lang="sa-Latn">√ṛdhu~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-04-0161"></a>`04.0161` | <i lang="sa-Latn">√gṛdhu~</i> | <i lang="sa-Latn">abhikāṅkṣāyām</i> |

<a id="gana-05"></a>
## Gaṇa 5 — <i lang="sa-Latn">svādi-gaṇaḥ</i> · <span lang="sa-Deva">स्वादिगणः</span>

[Derivation chapter 5](#chapter-05) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-05-0001"></a>`05.0001` | <i lang="sa-Latn">√ṣu\ñ</i> | <i lang="sa-Latn">abhiṣave</i> |
| <a id="dhatu-05-0002"></a>`05.0002` | <i lang="sa-Latn">√ṣi\ñ</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-05-0003"></a>`05.0003` | <i lang="sa-Latn">√śi\ñ</i> | <i lang="sa-Latn">niśāne</i> |
| <a id="dhatu-05-0004"></a>`05.0004` | <i lang="sa-Latn">√ḍumi\ñ</i> | <i lang="sa-Latn">prakṣepaṇe</i> |
| <a id="dhatu-05-0005"></a>`05.0005` | <i lang="sa-Latn">√ci\ñ</i> | <i lang="sa-Latn">cayane</i> |
| <a id="dhatu-05-0006"></a>`05.0006` | <i lang="sa-Latn">√stṛ\ñ</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-05-0007"></a>`05.0007` | <i lang="sa-Latn">√kṛ\ñ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0008"></a>`05.0008` | <i lang="sa-Latn">√vṛñ</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-05-0009"></a>`05.0009` | <i lang="sa-Latn">√dhu\ñ</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-05-0010"></a>`05.0010` | <i lang="sa-Latn">√dhūñ</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-05-0011"></a>`05.0011` | <i lang="sa-Latn">√ṭudu\</i> | <i lang="sa-Latn">upatāpe</i> |
| <a id="dhatu-05-0012"></a>`05.0012` | <i lang="sa-Latn">√hi\</i> | <i lang="sa-Latn">gatau vṛddhau ca</i> |
| <a id="dhatu-05-0013"></a>`05.0013` | <i lang="sa-Latn">√pṛ\</i> | <i lang="sa-Latn">prītau</i> |
| <a id="dhatu-05-0014"></a>`05.0014` | <i lang="sa-Latn">√spṛ\</i> | <i lang="sa-Latn">prītipālanayoḥ prīticalanayośca</i> |
| <a id="dhatu-05-0015"></a>`05.0015` | <i lang="sa-Latn">√smṛ\</i> | <i lang="sa-Latn">prītibalanayoḥ</i> |
| <a id="dhatu-05-0016"></a>`05.0016` | <i lang="sa-Latn">√ā\pḷ~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-05-0017"></a>`05.0017` | <i lang="sa-Latn">√śa\kḷ~</i> | <i lang="sa-Latn">śaktau</i> |
| <a id="dhatu-05-0018"></a>`05.0018` | <i lang="sa-Latn">√rā\dha~</i> | <i lang="sa-Latn">saṃsiddhau</i> |
| <a id="dhatu-05-0019"></a>`05.0019` | <i lang="sa-Latn">√sā\dha~</i> | <i lang="sa-Latn">saṃsiddhau</i> |
| <a id="dhatu-05-0020"></a>`05.0020` | <i lang="sa-Latn">√aśū~\</i> | <i lang="sa-Latn">vyāptau saṅghāte ca</i> |
| <a id="dhatu-05-0021"></a>`05.0021` | <i lang="sa-Latn">√ṣṭigha~\</i> | <i lang="sa-Latn">āskandane</i> |
| <a id="dhatu-05-0022"></a>`05.0022` | <i lang="sa-Latn">√tika~</i> | <i lang="sa-Latn">āskandane gatau ca</i> |
| <a id="dhatu-05-0023"></a>`05.0023` | <i lang="sa-Latn">√tiga~</i> | <i lang="sa-Latn">āskandane gatau ca</i> |
| <a id="dhatu-05-0024"></a>`05.0024` | <i lang="sa-Latn">√ṣagha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0025"></a>`05.0025` | <i lang="sa-Latn">√ñidhṛṣā~</i> | <i lang="sa-Latn">prāgalbhye</i> |
| <a id="dhatu-05-0026"></a>`05.0026` | <i lang="sa-Latn">√danbhu~</i> | <i lang="sa-Latn">dambhane</i> |
| <a id="dhatu-05-0027"></a>`05.0027` | <i lang="sa-Latn">√ṛdhu~</i> | <i lang="sa-Latn">vṛddhau</i> |
| <a id="dhatu-05-0028"></a>`05.0028` | <i lang="sa-Latn">√tṛpa~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-05-0029"></a>`05.0029` | <i lang="sa-Latn">√aha~</i> | <i lang="sa-Latn">vyāptau</i> |
| <a id="dhatu-05-0030"></a>`05.0030` | <i lang="sa-Latn">√dagha~</i> | <i lang="sa-Latn">ghātane pālane ca</i> |
| <a id="dhatu-05-0031"></a>`05.0031` | <i lang="sa-Latn">√camu~</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-05-0032"></a>`05.0032` | <i lang="sa-Latn">√ri\</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0033"></a>`05.0033` | <i lang="sa-Latn">√kṣi\</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0034"></a>`05.0034` | <i lang="sa-Latn">√ciri</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0035"></a>`05.0035` | <i lang="sa-Latn">√jiri</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0036"></a>`05.0036` | <i lang="sa-Latn">√dāśa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0037"></a>`05.0037` | <i lang="sa-Latn">√dṛ\</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-05-0038"></a>`05.0038` | <i lang="sa-Latn">√ṛ\kṣi</i> | <i lang="sa-Latn">hiṃsāyām</i> |

<a id="gana-06"></a>
## Gaṇa 6 — <i lang="sa-Latn">tudādi-gaṇaḥ</i> · <span lang="sa-Deva">तुदादिगणः</span>

[Derivation chapter 6](#chapter-06) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-06-0001"></a>`06.0001` | <i lang="sa-Latn">√tu\da~^</i> | <i lang="sa-Latn">vyathane</i> |
| <a id="dhatu-06-0002"></a>`06.0002` | <i lang="sa-Latn">√ṇu\da~^</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-06-0003"></a>`06.0003` | <i lang="sa-Latn">√di\śa~^</i> | <i lang="sa-Latn">atisarjane</i> |
| <a id="dhatu-06-0004"></a>`06.0004` | <i lang="sa-Latn">√bhra\sja~^</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-06-0005"></a>`06.0005` | <i lang="sa-Latn">√kṣi\pa~^</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-06-0006"></a>`06.0006` | <i lang="sa-Latn">√kṛ\ṣa~^</i> | <i lang="sa-Latn">vilekhane</i> |
| <a id="dhatu-06-0007"></a>`06.0007` | <i lang="sa-Latn">√ṛṣī~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0008"></a>`06.0008` | <i lang="sa-Latn">√juṣī~\</i> | <i lang="sa-Latn">prītisevanayoḥ</i> |
| <a id="dhatu-06-0009"></a>`06.0009` | <i lang="sa-Latn">√o~vijī~\</i> | <i lang="sa-Latn">bhayacalanayoḥ</i> |
| <a id="dhatu-06-0010"></a>`06.0010` | <i lang="sa-Latn">√o~lajī~\</i> | <i lang="sa-Latn">vrīḍāyām</i> |
| <a id="dhatu-06-0011"></a>`06.0011` | <i lang="sa-Latn">√o~lasjī~\</i> | <i lang="sa-Latn">vrīḍāyām</i> |
| <a id="dhatu-06-0012"></a>`06.0012` | <i lang="sa-Latn">√o~vrascū~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0013"></a>`06.0013` | <i lang="sa-Latn">√vyaca~</i> | <i lang="sa-Latn">vyājīkaraṇe</i> |
| <a id="dhatu-06-0014"></a>`06.0014` | <i lang="sa-Latn">√uchi~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-06-0015"></a>`06.0015` | <i lang="sa-Latn">√uchī~</i> | <i lang="sa-Latn">vivāse</i> |
| <a id="dhatu-06-0016"></a>`06.0016` | <i lang="sa-Latn">√ṛcha~</i> | <i lang="sa-Latn">gatīndriyapralayamūrtibhāveṣu</i> |
| <a id="dhatu-06-0017"></a>`06.0017` | <i lang="sa-Latn">√micha~</i> | <i lang="sa-Latn">utkleśe</i> |
| <a id="dhatu-06-0018"></a>`06.0018` | <i lang="sa-Latn">√jarja~</i> | <i lang="sa-Latn">paribhāṣaṇabhartsanayoḥ</i> |
| <a id="dhatu-06-0019"></a>`06.0019` | <i lang="sa-Latn">√carca~</i> | <i lang="sa-Latn">paribhāṣaṇabhartsanayoḥ</i> |
| <a id="dhatu-06-0020"></a>`06.0020` | <i lang="sa-Latn">√jharjha~</i> | <i lang="sa-Latn">paribhāṣaṇabhartsanayoḥ</i> |
| <a id="dhatu-06-0021"></a>`06.0021` | <i lang="sa-Latn">√tvaca~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0022"></a>`06.0022` | <i lang="sa-Latn">√ṛca~</i> | <i lang="sa-Latn">stutau dīptau ca</i> |
| <a id="dhatu-06-0023"></a>`06.0023` | <i lang="sa-Latn">√ubja~</i> | <i lang="sa-Latn">ārjave</i> |
| <a id="dhatu-06-0024"></a>`06.0024` | <i lang="sa-Latn">√ujjha~</i> | <i lang="sa-Latn">utsarge</i> |
| <a id="dhatu-06-0025"></a>`06.0025` | <i lang="sa-Latn">√lubha~</i> | <i lang="sa-Latn">vimohane</i> |
| <a id="dhatu-06-0026"></a>`06.0026` | <i lang="sa-Latn">√ripha~</i> | <i lang="sa-Latn">katthanayuddhanindāhiṃsādāneṣu</i> |
| <a id="dhatu-06-0027"></a>`06.0027` | <i lang="sa-Latn">√riha~</i> | <i lang="sa-Latn">katthanayuddhanindāhiṃsādāneṣu</i> |
| <a id="dhatu-06-0028"></a>`06.0028` | <i lang="sa-Latn">√tṛpa~</i> | <i lang="sa-Latn">tṛptau</i> |
| <a id="dhatu-06-0029"></a>`06.0029` | <i lang="sa-Latn">√ṛha~</i> | <i lang="sa-Latn">katthanayuddhanindāhiṃsādāneṣu</i> |
| <a id="dhatu-06-0030"></a>`06.0030` | <i lang="sa-Latn">√tṛpha~</i> | <i lang="sa-Latn">tṛptau</i> |
| <a id="dhatu-06-0031"></a>`06.0031` | <i lang="sa-Latn">√tṛnpha~</i> | <i lang="sa-Latn">tṛptau</i> |
| <a id="dhatu-06-0032"></a>`06.0032` | <i lang="sa-Latn">√tupa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0033"></a>`06.0033` | <i lang="sa-Latn">√tunpa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0034"></a>`06.0034` | <i lang="sa-Latn">√tupha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0035"></a>`06.0035` | <i lang="sa-Latn">√tunpha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0036"></a>`06.0036` | <i lang="sa-Latn">√dṛpa~</i> | <i lang="sa-Latn">utkleśe</i> |
| <a id="dhatu-06-0037"></a>`06.0037` | <i lang="sa-Latn">√stṛnhū~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0038"></a>`06.0038` | <i lang="sa-Latn">√dṛpha~</i> | <i lang="sa-Latn">utkleśe</i> |
| <a id="dhatu-06-0039"></a>`06.0039` | <i lang="sa-Latn">√dṛnpha~</i> | <i lang="sa-Latn">utkleśe</i> |
| <a id="dhatu-06-0040"></a>`06.0040` | <i lang="sa-Latn">√ṛpha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0041"></a>`06.0041` | <i lang="sa-Latn">√ṛnpha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0042"></a>`06.0042` | <i lang="sa-Latn">√gupha~</i> | <i lang="sa-Latn">granthe</i> |
| <a id="dhatu-06-0043"></a>`06.0043` | <i lang="sa-Latn">√gunpha~</i> | <i lang="sa-Latn">granthe</i> |
| <a id="dhatu-06-0044"></a>`06.0044` | <i lang="sa-Latn">√ubha~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-06-0045"></a>`06.0045` | <i lang="sa-Latn">√unbha~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-06-0046"></a>`06.0046` | <i lang="sa-Latn">√śubha~</i> | <i lang="sa-Latn">śobhāyām</i> |
| <a id="dhatu-06-0047"></a>`06.0047` | <i lang="sa-Latn">√śunbha~</i> | <i lang="sa-Latn">śobhāyām</i> |
| <a id="dhatu-06-0048"></a>`06.0048` | <i lang="sa-Latn">√dṛbhī~</i> | <i lang="sa-Latn">granthe</i> |
| <a id="dhatu-06-0049"></a>`06.0049` | <i lang="sa-Latn">√cṛtī~</i> | <i lang="sa-Latn">hiṃsāgranthanayoḥ</i> |
| <a id="dhatu-06-0050"></a>`06.0050` | <i lang="sa-Latn">√vidha~</i> | <i lang="sa-Latn">vidhāne</i> |
| <a id="dhatu-06-0051"></a>`06.0051` | <i lang="sa-Latn">√juḍa~</i> | <i lang="sa-Latn">gatau bandhane ca</i> |
| <a id="dhatu-06-0052"></a>`06.0052` | <i lang="sa-Latn">√juna~</i> | <i lang="sa-Latn">gatau bandhane ca</i> |
| <a id="dhatu-06-0053"></a>`06.0053` | <i lang="sa-Latn">√mṛḍa~</i> | <i lang="sa-Latn">sukhane</i> |
| <a id="dhatu-06-0054"></a>`06.0054` | <i lang="sa-Latn">√pṛḍa~</i> | <i lang="sa-Latn">sukhane</i> |
| <a id="dhatu-06-0055"></a>`06.0055` | <i lang="sa-Latn">√pṛṇa~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-06-0056"></a>`06.0056` | <i lang="sa-Latn">√vṛṇa~</i> | <i lang="sa-Latn">prīṇane</i> |
| <a id="dhatu-06-0057"></a>`06.0057` | <i lang="sa-Latn">√mṛṇa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0058"></a>`06.0058` | <i lang="sa-Latn">√tuṇa~</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-06-0059"></a>`06.0059` | <i lang="sa-Latn">√puṇa~</i> | <i lang="sa-Latn">karmaṇi śubhe</i> |
| <a id="dhatu-06-0060"></a>`06.0060` | <i lang="sa-Latn">√muṇa~</i> | <i lang="sa-Latn">pratijñāne</i> |
| <a id="dhatu-06-0061"></a>`06.0061` | <i lang="sa-Latn">√kuṇa~</i> | <i lang="sa-Latn">śabdopakaraṇayoḥ</i> |
| <a id="dhatu-06-0062"></a>`06.0062` | <i lang="sa-Latn">√śuna~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0063"></a>`06.0063` | <i lang="sa-Latn">√druṇa~</i> | <i lang="sa-Latn">hiṃsāgatikauṭilyeṣu</i> |
| <a id="dhatu-06-0064"></a>`06.0064` | <i lang="sa-Latn">√ghuṇa~</i> | <i lang="sa-Latn">bhramaṇe</i> |
| <a id="dhatu-06-0065"></a>`06.0065` | <i lang="sa-Latn">√ghūrṇa~</i> | <i lang="sa-Latn">bhramaṇe</i> |
| <a id="dhatu-06-0066"></a>`06.0066` | <i lang="sa-Latn">√ṣura~</i> | <i lang="sa-Latn">aiśvaryadīptyoḥ</i> |
| <a id="dhatu-06-0067"></a>`06.0067` | <i lang="sa-Latn">√kura~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-06-0068"></a>`06.0068` | <i lang="sa-Latn">√khura~</i> | <i lang="sa-Latn">chedane khaṇḍane ca</i> |
| <a id="dhatu-06-0069"></a>`06.0069` | <i lang="sa-Latn">√mura~</i> | <i lang="sa-Latn">saṃveṣṭane pariveṣṭane ca</i> |
| <a id="dhatu-06-0070"></a>`06.0070` | <i lang="sa-Latn">√kṣura~</i> | <i lang="sa-Latn">vilekhane</i> |
| <a id="dhatu-06-0071"></a>`06.0071` | <i lang="sa-Latn">√ghura~</i> | <i lang="sa-Latn">bhīmārthaśabdayoḥ</i> |
| <a id="dhatu-06-0072"></a>`06.0072` | <i lang="sa-Latn">√pura~</i> | <i lang="sa-Latn">agragamane</i> |
| <a id="dhatu-06-0073"></a>`06.0073` | <i lang="sa-Latn">√vṛhū~</i> | <i lang="sa-Latn">udyamane</i> |
| <a id="dhatu-06-0074"></a>`06.0074` | <i lang="sa-Latn">√bṛhū~</i> | <i lang="sa-Latn">udyamane</i> |
| <a id="dhatu-06-0075"></a>`06.0075` | <i lang="sa-Latn">√tṛhū~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0076"></a>`06.0076` | <i lang="sa-Latn">√stṛhū~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0077"></a>`06.0077` | <i lang="sa-Latn">√tṛnhū~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0078"></a>`06.0078` | <i lang="sa-Latn">√iṣu~</i> | <i lang="sa-Latn">icchāyām</i> |
| <a id="dhatu-06-0079"></a>`06.0079` | <i lang="sa-Latn">√miṣa~</i> | <i lang="sa-Latn">spardhāyām</i> |
| <a id="dhatu-06-0080"></a>`06.0080` | <i lang="sa-Latn">√kila~</i> | <i lang="sa-Latn">śvaityakrīḍanayoḥ</i> |
| <a id="dhatu-06-0081"></a>`06.0081` | <i lang="sa-Latn">√tila~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-06-0082"></a>`06.0082` | <i lang="sa-Latn">√cila~</i> | <i lang="sa-Latn">vasane</i> |
| <a id="dhatu-06-0083"></a>`06.0083` | <i lang="sa-Latn">√cala~</i> | <i lang="sa-Latn">vilasane vikasane ca</i> |
| <a id="dhatu-06-0084"></a>`06.0084` | <i lang="sa-Latn">√ila~</i> | <i lang="sa-Latn">svapnakṣepaṇayoḥ</i> |
| <a id="dhatu-06-0085"></a>`06.0085` | <i lang="sa-Latn">√vila~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0086"></a>`06.0086` | <i lang="sa-Latn">√bila~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-06-0087"></a>`06.0087` | <i lang="sa-Latn">√ṇila~</i> | <i lang="sa-Latn">gahane</i> |
| <a id="dhatu-06-0088"></a>`06.0088` | <i lang="sa-Latn">√hila~</i> | <i lang="sa-Latn">bhāvakaraṇe</i> |
| <a id="dhatu-06-0089"></a>`06.0089` | <i lang="sa-Latn">√śila~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-06-0090"></a>`06.0090` | <i lang="sa-Latn">√ṣila~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-06-0091"></a>`06.0091` | <i lang="sa-Latn">√mila~</i> | <i lang="sa-Latn">śleṣaṇe</i> |
| <a id="dhatu-06-0092"></a>`06.0092` | <i lang="sa-Latn">√likha~</i> | <i lang="sa-Latn">akṣaravinyāse</i> |
| <a id="dhatu-06-0093"></a>`06.0093` | <i lang="sa-Latn">√kuṭa~</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-06-0094"></a>`06.0094` | <i lang="sa-Latn">√puṭa~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-06-0095"></a>`06.0095` | <i lang="sa-Latn">√kuca~</i> | <i lang="sa-Latn">saṅkocane</i> |
| <a id="dhatu-06-0096"></a>`06.0096` | <i lang="sa-Latn">√guja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-06-0097"></a>`06.0097` | <i lang="sa-Latn">√guḍa~</i> | <i lang="sa-Latn">rakṣāyām</i> |
| <a id="dhatu-06-0098"></a>`06.0098` | <i lang="sa-Latn">√ḍipa~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-06-0099"></a>`06.0099` | <i lang="sa-Latn">√chura~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0100"></a>`06.0100` | <i lang="sa-Latn">√sphuṭa~</i> | <i lang="sa-Latn">vikasane</i> |
| <a id="dhatu-06-0101"></a>`06.0101` | <i lang="sa-Latn">√muṭa~</i> | <i lang="sa-Latn">ākṣepamardanayoḥ</i> |
| <a id="dhatu-06-0102"></a>`06.0102` | <i lang="sa-Latn">√truṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0103"></a>`06.0103` | <i lang="sa-Latn">√tuṭa~</i> | <i lang="sa-Latn">kalahakarmaṇi</i> |
| <a id="dhatu-06-0104"></a>`06.0104` | <i lang="sa-Latn">√cuṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0105"></a>`06.0105` | <i lang="sa-Latn">√chuṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0106"></a>`06.0106` | <i lang="sa-Latn">√juḍa~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-06-0107"></a>`06.0107` | <i lang="sa-Latn">√juṭa~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-06-0108"></a>`06.0108` | <i lang="sa-Latn">√kaḍa~</i> | <i lang="sa-Latn">made</i> |
| <a id="dhatu-06-0109"></a>`06.0109` | <i lang="sa-Latn">√luṭa~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-06-0110"></a>`06.0110` | <i lang="sa-Latn">√luṭha~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-06-0111"></a>`06.0111` | <i lang="sa-Latn">√kaḍa~</i> | <i lang="sa-Latn">ghasane</i> |
| <a id="dhatu-06-0112"></a>`06.0112` | <i lang="sa-Latn">√kṛḍa~</i> | <i lang="sa-Latn">ghanatve</i> |
| <a id="dhatu-06-0113"></a>`06.0113` | <i lang="sa-Latn">√kuḍa~</i> | <i lang="sa-Latn">bālye</i> |
| <a id="dhatu-06-0114"></a>`06.0114` | <i lang="sa-Latn">√puḍa~</i> | <i lang="sa-Latn">utsarge</i> |
| <a id="dhatu-06-0115"></a>`06.0115` | <i lang="sa-Latn">√ghuṭa~</i> | <i lang="sa-Latn">pratighāte</i> |
| <a id="dhatu-06-0116"></a>`06.0116` | <i lang="sa-Latn">√tuḍa~</i> | <i lang="sa-Latn">toḍane</i> |
| <a id="dhatu-06-0117"></a>`06.0117` | <i lang="sa-Latn">√thuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0118"></a>`06.0118` | <i lang="sa-Latn">√sthuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0119"></a>`06.0119` | <i lang="sa-Latn">√khuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0120"></a>`06.0120` | <i lang="sa-Latn">√chuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0121"></a>`06.0121` | <i lang="sa-Latn">√sphura~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-06-0122"></a>`06.0122` | <i lang="sa-Latn">√sphula~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-06-0123"></a>`06.0123` | <i lang="sa-Latn">√sphara~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-06-0124"></a>`06.0124` | <i lang="sa-Latn">√sphala~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-06-0125"></a>`06.0125` | <i lang="sa-Latn">√sphuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0126"></a>`06.0126` | <i lang="sa-Latn">√cuḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0127"></a>`06.0127` | <i lang="sa-Latn">√vruḍa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-06-0128"></a>`06.0128` | <i lang="sa-Latn">√kruḍa~</i> | <i lang="sa-Latn">nimajjane</i> |
| <a id="dhatu-06-0129"></a>`06.0129` | <i lang="sa-Latn">√bhṛḍa~</i> | <i lang="sa-Latn">nimajjane</i> |
| <a id="dhatu-06-0130"></a>`06.0130` | <i lang="sa-Latn">√huḍa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-06-0131"></a>`06.0131` | <i lang="sa-Latn">√gurī~\</i> | <i lang="sa-Latn">udyamane</i> |
| <a id="dhatu-06-0132"></a>`06.0132` | <i lang="sa-Latn">√ṇū</i> | <i lang="sa-Latn">stavane</i> |
| <a id="dhatu-06-0133"></a>`06.0133` | <i lang="sa-Latn">√dhū</i> | <i lang="sa-Latn">vidhūnane</i> |
| <a id="dhatu-06-0134"></a>`06.0134` | <i lang="sa-Latn">√gu\</i> | <i lang="sa-Latn">purīṣotsarge</i> |
| <a id="dhatu-06-0135"></a>`06.0135` | <i lang="sa-Latn">√dhru\</i> | <i lang="sa-Latn">gatisthairyayoḥ</i> |
| <a id="dhatu-06-0136"></a>`06.0136` | <i lang="sa-Latn">√ku\ṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-06-0137"></a>`06.0137` | <i lang="sa-Latn">√kūṅ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-06-0138"></a>`06.0138` | <i lang="sa-Latn">√pṛ\ṅ</i> | <i lang="sa-Latn">vyāyāme</i> |
| <a id="dhatu-06-0139"></a>`06.0139` | <i lang="sa-Latn">√mṛ\ṅ</i> | <i lang="sa-Latn">prāṇatyāge</i> |
| <a id="dhatu-06-0140"></a>`06.0140` | <i lang="sa-Latn">√ri\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0141"></a>`06.0141` | <i lang="sa-Latn">√pi\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0142"></a>`06.0142` | <i lang="sa-Latn">√dhi\</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-06-0143"></a>`06.0143` | <i lang="sa-Latn">√kṣi\</i> | <i lang="sa-Latn">nivāsagatyoḥ</i> |
| <a id="dhatu-06-0144"></a>`06.0144` | <i lang="sa-Latn">√ṣū</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-06-0145"></a>`06.0145` | <i lang="sa-Latn">√kṝ</i> | <i lang="sa-Latn">vikṣepe</i> |
| <a id="dhatu-06-0146"></a>`06.0146` | <i lang="sa-Latn">√gṝ</i> | <i lang="sa-Latn">nigaraṇe</i> |
| <a id="dhatu-06-0147"></a>`06.0147` | <i lang="sa-Latn">√dṛ\ṅ</i> | <i lang="sa-Latn">ādare</i> |
| <a id="dhatu-06-0148"></a>`06.0148` | <i lang="sa-Latn">√dhṛ\ṅ</i> | <i lang="sa-Latn">avasthāne</i> |
| <a id="dhatu-06-0149"></a>`06.0149` | <i lang="sa-Latn">√pra\cha~</i> | <i lang="sa-Latn">jñīpsāyām</i> |
| <a id="dhatu-06-0150"></a>`06.0150` | <i lang="sa-Latn">√sṛ\ja~</i> | <i lang="sa-Latn">visarge</i> |
| <a id="dhatu-06-0151"></a>`06.0151` | <i lang="sa-Latn">√ṭuma\sjo~</i> | <i lang="sa-Latn">śuddhau</i> |
| <a id="dhatu-06-0152"></a>`06.0152` | <i lang="sa-Latn">√ru\jo~</i> | <i lang="sa-Latn">bhaṅge</i> |
| <a id="dhatu-06-0153"></a>`06.0153` | <i lang="sa-Latn">√bhu\jo~</i> | <i lang="sa-Latn">kauṭilye</i> |
| <a id="dhatu-06-0154"></a>`06.0154` | <i lang="sa-Latn">√chu\pa~</i> | <i lang="sa-Latn">sparśe</i> |
| <a id="dhatu-06-0155"></a>`06.0155` | <i lang="sa-Latn">√ru\śa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0156"></a>`06.0156` | <i lang="sa-Latn">√ri\śa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-06-0157"></a>`06.0157` | <i lang="sa-Latn">√li\śa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0158"></a>`06.0158` | <i lang="sa-Latn">√spṛ\śa~</i> | <i lang="sa-Latn">saṃsparśane</i> |
| <a id="dhatu-06-0159"></a>`06.0159` | <i lang="sa-Latn">√vicha~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-06-0160"></a>`06.0160` | <i lang="sa-Latn">√vi\śa~</i> | <i lang="sa-Latn">praveśane</i> |
| <a id="dhatu-06-0161"></a>`06.0161` | <i lang="sa-Latn">√mṛ\śa~</i> | <i lang="sa-Latn">āmarśane</i> |
| <a id="dhatu-06-0162"></a>`06.0162` | <i lang="sa-Latn">√ṇu\da~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-06-0163"></a>`06.0163` | <i lang="sa-Latn">√ṣa\dḷ~</i> | <i lang="sa-Latn">viśaraṇagatyavasādaneṣu</i> |
| <a id="dhatu-06-0164"></a>`06.0164` | <i lang="sa-Latn">√śa\dḷ~</i> | <i lang="sa-Latn">śātane</i> |
| <a id="dhatu-06-0165"></a>`06.0165` | <i lang="sa-Latn">√mila~^</i> | <i lang="sa-Latn">saṅgame</i> |
| <a id="dhatu-06-0166"></a>`06.0166` | <i lang="sa-Latn">√mu\cḷ~^</i> | <i lang="sa-Latn">mokṣaṇe</i> |
| <a id="dhatu-06-0167"></a>`06.0167` | <i lang="sa-Latn">√lu\pḷ~^</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0168"></a>`06.0168` | <i lang="sa-Latn">√vi\dḷ~^</i> | <i lang="sa-Latn">lābhe</i> |
| <a id="dhatu-06-0169"></a>`06.0169` | <i lang="sa-Latn">√li\pa~^</i> | <i lang="sa-Latn">upadehe</i> |
| <a id="dhatu-06-0170"></a>`06.0170` | <i lang="sa-Latn">√ṣi\ca~^</i> | <i lang="sa-Latn">kṣaraṇe</i> |
| <a id="dhatu-06-0171"></a>`06.0171` | <i lang="sa-Latn">√kṛtī~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-06-0172"></a>`06.0172` | <i lang="sa-Latn">√khi\da~</i> | <i lang="sa-Latn">parighāte</i> |
| <a id="dhatu-06-0173"></a>`06.0173` | <i lang="sa-Latn">√piśa~</i> | <i lang="sa-Latn">avayave</i> |
| <a id="dhatu-06-0174"></a>`06.0174` | <i lang="sa-Latn">√phula~</i> | <i lang="sa-Latn">sañcalane</i> |

<a id="gana-07"></a>
## Gaṇa 7 — <i lang="sa-Latn">rudhādi-gaṇaḥ</i> · <span lang="sa-Deva">रुधादिगणः</span>

[Derivation chapter 7](#chapter-07) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-07-0001"></a>`07.0001` | <i lang="sa-Latn">√ru\dhi~^r</i> | <i lang="sa-Latn">āvaraṇe</i> |
| <a id="dhatu-07-0002"></a>`07.0002` | <i lang="sa-Latn">√bhi\di~^r</i> | <i lang="sa-Latn">vidāraṇe</i> |
| <a id="dhatu-07-0003"></a>`07.0003` | <i lang="sa-Latn">√chi\di~^r</i> | <i lang="sa-Latn">dvaidhīkaraṇe</i> |
| <a id="dhatu-07-0004"></a>`07.0004` | <i lang="sa-Latn">√ri\ci~^r</i> | <i lang="sa-Latn">virecane</i> |
| <a id="dhatu-07-0005"></a>`07.0005` | <i lang="sa-Latn">√vi\ci~^r</i> | <i lang="sa-Latn">pṛthagbhāve</i> |
| <a id="dhatu-07-0006"></a>`07.0006` | <i lang="sa-Latn">√kṣu\di~^r</i> | <i lang="sa-Latn">sampeṣaṇe</i> |
| <a id="dhatu-07-0007"></a>`07.0007` | <i lang="sa-Latn">√yu\ji~^r</i> | <i lang="sa-Latn">yoge</i> |
| <a id="dhatu-07-0008"></a>`07.0008` | <i lang="sa-Latn">√u~chṛdi~^r</i> | <i lang="sa-Latn">dīptidevanayoḥ</i> |
| <a id="dhatu-07-0009"></a>`07.0009` | <i lang="sa-Latn">√u~tṛdi~^r</i> | <i lang="sa-Latn">hiṃsānādarayoḥ</i> |
| <a id="dhatu-07-0010"></a>`07.0010` | <i lang="sa-Latn">√kṛtī~</i> | <i lang="sa-Latn">veṣṭane</i> |
| <a id="dhatu-07-0011"></a>`07.0011` | <i lang="sa-Latn">√ñiindhī~\</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-07-0012"></a>`07.0012` | <i lang="sa-Latn">√khi\da~\</i> | <i lang="sa-Latn">dainye</i> |
| <a id="dhatu-07-0013"></a>`07.0013` | <i lang="sa-Latn">√vi\da~\</i> | <i lang="sa-Latn">vicāraṇe</i> |
| <a id="dhatu-07-0014"></a>`07.0014` | <i lang="sa-Latn">√śi\ṣḷ~</i> | <i lang="sa-Latn">viśeṣaṇe</i> |
| <a id="dhatu-07-0015"></a>`07.0015` | <i lang="sa-Latn">√pi\ṣḷ~</i> | <i lang="sa-Latn">sañcūrṇane hiṃsāyām ca</i> |
| <a id="dhatu-07-0016"></a>`07.0016` | <i lang="sa-Latn">√bha\njo~</i> | <i lang="sa-Latn">āmardane</i> |
| <a id="dhatu-07-0017"></a>`07.0017` | <i lang="sa-Latn">√bhu\ja~</i> | <i lang="sa-Latn">pālanābhyavahārayoḥ</i> |
| <a id="dhatu-07-0018"></a>`07.0018` | <i lang="sa-Latn">√tṛha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-07-0019"></a>`07.0019` | <i lang="sa-Latn">√hisi~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-07-0020"></a>`07.0020` | <i lang="sa-Latn">√undī~</i> | <i lang="sa-Latn">kledane</i> |
| <a id="dhatu-07-0021"></a>`07.0021` | <i lang="sa-Latn">√anjū~</i> | <i lang="sa-Latn">vyaktimrakṣaṇakāntigatiṣu</i> |
| <a id="dhatu-07-0022"></a>`07.0022` | <i lang="sa-Latn">√tancū~</i> | <i lang="sa-Latn">saṅkocane</i> |
| <a id="dhatu-07-0023"></a>`07.0023` | <i lang="sa-Latn">√o~vijī~</i> | <i lang="sa-Latn">bhayacalanayoḥ</i> |
| <a id="dhatu-07-0024"></a>`07.0024` | <i lang="sa-Latn">√vṛjī~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-07-0025"></a>`07.0025` | <i lang="sa-Latn">√pṛcī~</i> | <i lang="sa-Latn">samparke</i> |

<a id="gana-08"></a>
## Gaṇa 8 — <i lang="sa-Latn">tanādi-gaṇaḥ</i> · <span lang="sa-Deva">तनादिगणः</span>

[Derivation chapter 8](#chapter-08) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-08-0001"></a>`08.0001` | <i lang="sa-Latn">√tanu~^</i> | <i lang="sa-Latn">vistāre</i> |
| <a id="dhatu-08-0002"></a>`08.0002` | <i lang="sa-Latn">√ṣaṇu~^</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-08-0003"></a>`08.0003` | <i lang="sa-Latn">√kṣaṇu~^</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-08-0004"></a>`08.0004` | <i lang="sa-Latn">√kṣiṇu~^</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-08-0005"></a>`08.0005` | <i lang="sa-Latn">√ṛṇu~^</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-08-0006"></a>`08.0006` | <i lang="sa-Latn">√tṛṇu~^</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-08-0007"></a>`08.0007` | <i lang="sa-Latn">√ghṛṇu~^</i> | <i lang="sa-Latn">dīptau</i> |
| <a id="dhatu-08-0008"></a>`08.0008` | <i lang="sa-Latn">√vanu~\</i> | <i lang="sa-Latn">yācane</i> |
| <a id="dhatu-08-0009"></a>`08.0009` | <i lang="sa-Latn">√manu~\</i> | <i lang="sa-Latn">avabodhane</i> |
| <a id="dhatu-08-0010"></a>`08.0010` | <i lang="sa-Latn">√ḍukṛ\ñ</i> | <i lang="sa-Latn">karaṇe</i> |

<a id="gana-09"></a>
## Gaṇa 9 — <i lang="sa-Latn">kryādi-gaṇaḥ</i> · <span lang="sa-Deva">क्र्यादिगणः</span>

[Derivation chapter 9](#chapter-09) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-09-0001"></a>`09.0001` | <i lang="sa-Latn">√ḍukrī\ñ</i> | <i lang="sa-Latn">dravyavinimaye</i> |
| <a id="dhatu-09-0002"></a>`09.0002` | <i lang="sa-Latn">√prī\ñ</i> | <i lang="sa-Latn">tarpaṇe kāntau ca</i> |
| <a id="dhatu-09-0003"></a>`09.0003` | <i lang="sa-Latn">√śrī\ñ</i> | <i lang="sa-Latn">pāke</i> |
| <a id="dhatu-09-0004"></a>`09.0004` | <i lang="sa-Latn">√mī\ñ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0005"></a>`09.0005` | <i lang="sa-Latn">√ṣi\ñ</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-09-0006"></a>`09.0006` | <i lang="sa-Latn">√sku\ñ</i> | <i lang="sa-Latn">āpravaṇe</i> |
| <a id="dhatu-09-0007"></a>`09.0007` | <i lang="sa-Latn">√stanbhu~</i> | <i lang="sa-Latn">rodhane stambhane ca</i> |
| <a id="dhatu-09-0008"></a>`09.0008` | <i lang="sa-Latn">√stunbhu~</i> | <i lang="sa-Latn">rodhane niṣkoṣaṇe ca</i> |
| <a id="dhatu-09-0009"></a>`09.0009` | <i lang="sa-Latn">√skanbhu~</i> | <i lang="sa-Latn">rodhane stambhane ca</i> |
| <a id="dhatu-09-0010"></a>`09.0010` | <i lang="sa-Latn">√skunbhu~</i> | <i lang="sa-Latn">rodhane dhāraṇe ca</i> |
| <a id="dhatu-09-0011"></a>`09.0011` | <i lang="sa-Latn">√yu\ñ</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-09-0012"></a>`09.0012` | <i lang="sa-Latn">√knūñ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-09-0013"></a>`09.0013` | <i lang="sa-Latn">√drūñ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0014"></a>`09.0014` | <i lang="sa-Latn">√pūñ</i> | <i lang="sa-Latn">pavane</i> |
| <a id="dhatu-09-0015"></a>`09.0015` | <i lang="sa-Latn">√śṝñ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0016"></a>`09.0016` | <i lang="sa-Latn">√lūñ</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-09-0017"></a>`09.0017` | <i lang="sa-Latn">√stṝñ</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-09-0018"></a>`09.0018` | <i lang="sa-Latn">√kṝñ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0019"></a>`09.0019` | <i lang="sa-Latn">√vṝñ</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0020"></a>`09.0020` | <i lang="sa-Latn">√dhūñ</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-09-0021"></a>`09.0021` | <i lang="sa-Latn">√śṝ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0022"></a>`09.0022` | <i lang="sa-Latn">√pṝ</i> | <i lang="sa-Latn">pālanapūraṇayoḥ</i> |
| <a id="dhatu-09-0023"></a>`09.0023` | <i lang="sa-Latn">√vṝ</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0024"></a>`09.0024` | <i lang="sa-Latn">√bhṝ</i> | <i lang="sa-Latn">bhartsane</i> |
| <a id="dhatu-09-0025"></a>`09.0025` | <i lang="sa-Latn">√mṝ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0026"></a>`09.0026` | <i lang="sa-Latn">√dṝ</i> | <i lang="sa-Latn">vidāraṇe</i> |
| <a id="dhatu-09-0027"></a>`09.0027` | <i lang="sa-Latn">√jṝ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-09-0028"></a>`09.0028` | <i lang="sa-Latn">√jhṝ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-09-0029"></a>`09.0029` | <i lang="sa-Latn">√dhṝ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-09-0030"></a>`09.0030` | <i lang="sa-Latn">√nṝ</i> | <i lang="sa-Latn">naye</i> |
| <a id="dhatu-09-0031"></a>`09.0031` | <i lang="sa-Latn">√kṝ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0032"></a>`09.0032` | <i lang="sa-Latn">√ṝ</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-09-0033"></a>`09.0033` | <i lang="sa-Latn">√gṝ</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-09-0034"></a>`09.0034` | <i lang="sa-Latn">√jyā\</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-09-0035"></a>`09.0035` | <i lang="sa-Latn">√rī\</i> | <i lang="sa-Latn">gatireṣaṇayoḥ</i> |
| <a id="dhatu-09-0036"></a>`09.0036` | <i lang="sa-Latn">√lī\</i> | <i lang="sa-Latn">śleṣaṇe</i> |
| <a id="dhatu-09-0037"></a>`09.0037` | <i lang="sa-Latn">√vlī\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0038"></a>`09.0038` | <i lang="sa-Latn">√blī\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0039"></a>`09.0039` | <i lang="sa-Latn">√plī\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-09-0040"></a>`09.0040` | <i lang="sa-Latn">√vrī\</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0041"></a>`09.0041` | <i lang="sa-Latn">√bhrī\</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-09-0042"></a>`09.0042` | <i lang="sa-Latn">√kṣī\ṣ</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0043"></a>`09.0043` | <i lang="sa-Latn">√jñā\</i> | <i lang="sa-Latn">avabodhane</i> |
| <a id="dhatu-09-0044"></a>`09.0044` | <i lang="sa-Latn">√ba\ndha~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-09-0045"></a>`09.0045` | <i lang="sa-Latn">√vṛṅ</i> | <i lang="sa-Latn">sambhaktau</i> |
| <a id="dhatu-09-0046"></a>`09.0046` | <i lang="sa-Latn">√śrantha~</i> | <i lang="sa-Latn">vimocanapratiharṣayoḥ</i> |
| <a id="dhatu-09-0047"></a>`09.0047` | <i lang="sa-Latn">√mantha~</i> | <i lang="sa-Latn">viloḍane</i> |
| <a id="dhatu-09-0048"></a>`09.0048` | <i lang="sa-Latn">√śrantha~</i> | <i lang="sa-Latn">sandarbhe</i> |
| <a id="dhatu-09-0049"></a>`09.0049` | <i lang="sa-Latn">√grantha~</i> | <i lang="sa-Latn">sandarbhe</i> |
| <a id="dhatu-09-0050"></a>`09.0050` | <i lang="sa-Latn">√kuntha~</i> | <i lang="sa-Latn">saṃśleṣaṇe</i> |
| <a id="dhatu-09-0051"></a>`09.0051` | <i lang="sa-Latn">√mṛda~</i> | <i lang="sa-Latn">kṣode</i> |
| <a id="dhatu-09-0052"></a>`09.0052` | <i lang="sa-Latn">√mṛḍa~</i> | <i lang="sa-Latn">kṣode sukhe ca</i> |
| <a id="dhatu-09-0053"></a>`09.0053` | <i lang="sa-Latn">√gudha~</i> | <i lang="sa-Latn">roṣe</i> |
| <a id="dhatu-09-0054"></a>`09.0054` | <i lang="sa-Latn">√kuṣa~</i> | <i lang="sa-Latn">niṣkarṣe</i> |
| <a id="dhatu-09-0055"></a>`09.0055` | <i lang="sa-Latn">√kṣubha~</i> | <i lang="sa-Latn">sañcalane</i> |
| <a id="dhatu-09-0056"></a>`09.0056` | <i lang="sa-Latn">√ṇabha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0057"></a>`09.0057` | <i lang="sa-Latn">√tubha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-09-0058"></a>`09.0058` | <i lang="sa-Latn">√kliśū~</i> | <i lang="sa-Latn">vibādhane</i> |
| <a id="dhatu-09-0059"></a>`09.0059` | <i lang="sa-Latn">√aśa~</i> | <i lang="sa-Latn">bhojane</i> |
| <a id="dhatu-09-0060"></a>`09.0060` | <i lang="sa-Latn">√u~dhrasa~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-09-0061"></a>`09.0061` | <i lang="sa-Latn">√iṣa~</i> | <i lang="sa-Latn">ābhīkṣṇye</i> |
| <a id="dhatu-09-0062"></a>`09.0062` | <i lang="sa-Latn">√vi\ṣa~</i> | <i lang="sa-Latn">viprayoge</i> |
| <a id="dhatu-09-0063"></a>`09.0063` | <i lang="sa-Latn">√pruṣa~</i> | <i lang="sa-Latn">snehanasevanapūraṇeṣu</i> |
| <a id="dhatu-09-0064"></a>`09.0064` | <i lang="sa-Latn">√pluṣa~</i> | <i lang="sa-Latn">snehanasevanapūraṇeṣu</i> |
| <a id="dhatu-09-0065"></a>`09.0065` | <i lang="sa-Latn">√puṣa~</i> | <i lang="sa-Latn">puṣṭau</i> |
| <a id="dhatu-09-0066"></a>`09.0066` | <i lang="sa-Latn">√muṣa~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-09-0067"></a>`09.0067` | <i lang="sa-Latn">√khaca~</i> | <i lang="sa-Latn">bhūtaprādurbhāve</i> |
| <a id="dhatu-09-0068"></a>`09.0068` | <i lang="sa-Latn">√khava~</i> | <i lang="sa-Latn">bhūtaprādurbhāve</i> |
| <a id="dhatu-09-0069"></a>`09.0069` | <i lang="sa-Latn">√heṭha~</i> | <i lang="sa-Latn">bhūtaprādurbhāve</i> |
| <a id="dhatu-09-0070"></a>`09.0070` | <i lang="sa-Latn">√svṝ</i> | <i lang="sa-Latn">varaṇe</i> |
| <a id="dhatu-09-0071"></a>`09.0071` | <i lang="sa-Latn">√graha~^</i> | <i lang="sa-Latn">upādāne</i> |

<a id="gana-10"></a>
## Gaṇa 10 — <i lang="sa-Latn">curādi-gaṇaḥ</i> · <span lang="sa-Deva">चुरादिगणः</span>

[Derivation chapter 10](#chapter-10) · [↑ Contents](#toc)

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-10-0001"></a>`10.0001` | <i lang="sa-Latn">√cura~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-10-0002"></a>`10.0002` | <i lang="sa-Latn">√citi~</i> | <i lang="sa-Latn">smṛtyām</i> |
| <a id="dhatu-10-0003"></a>`10.0003` | <i lang="sa-Latn">√yatri~</i> | <i lang="sa-Latn">saṅkoce</i> |
| <a id="dhatu-10-0004"></a>`10.0004` | <i lang="sa-Latn">√sphuḍi~</i> | <i lang="sa-Latn">parihāse</i> |
| <a id="dhatu-10-0005"></a>`10.0005` | <i lang="sa-Latn">√sphuṭi~</i> | <i lang="sa-Latn">parihāse</i> |
| <a id="dhatu-10-0006"></a>`10.0006` | <i lang="sa-Latn">√lakṣa~</i> | <i lang="sa-Latn">darśanāṅkanayoḥ</i> |
| <a id="dhatu-10-0007"></a>`10.0007` | <i lang="sa-Latn">√kudri~</i> | <i lang="sa-Latn">anṛtabhāṣaṇe</i> |
| <a id="dhatu-10-0008"></a>`10.0008` | <i lang="sa-Latn">√kudṛ~</i> | <i lang="sa-Latn">anṛtabhāṣaṇe</i> |
| <a id="dhatu-10-0009"></a>`10.0009` | <i lang="sa-Latn">√spuḍi~</i> | <i lang="sa-Latn">parihāse</i> |
| <a id="dhatu-10-0010"></a>`10.0010` | <i lang="sa-Latn">√laḍa~</i> | <i lang="sa-Latn">upasevāyām</i> |
| <a id="dhatu-10-0011"></a>`10.0011` | <i lang="sa-Latn">√midi~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-10-0012"></a>`10.0012` | <i lang="sa-Latn">√mida~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-10-0013"></a>`10.0013` | <i lang="sa-Latn">√o~laḍi~</i> | <i lang="sa-Latn">utkṣepaṇe</i> |
| <a id="dhatu-10-0014"></a>`10.0014` | <i lang="sa-Latn">√olaḍi~</i> | <i lang="sa-Latn">utkṣepaṇe</i> |
| <a id="dhatu-10-0015"></a>`10.0015` | <i lang="sa-Latn">√jala~</i> | <i lang="sa-Latn">apavāraṇe</i> |
| <a id="dhatu-10-0016"></a>`10.0016` | <i lang="sa-Latn">√laja~</i> | <i lang="sa-Latn">apavāraṇe</i> |
| <a id="dhatu-10-0017"></a>`10.0017` | <i lang="sa-Latn">√pīḍa~</i> | <i lang="sa-Latn">avagāhane</i> |
| <a id="dhatu-10-0018"></a>`10.0018` | <i lang="sa-Latn">√naṭa~</i> | <i lang="sa-Latn">avaspandane</i> |
| <a id="dhatu-10-0019"></a>`10.0019` | <i lang="sa-Latn">√śratha~</i> | <i lang="sa-Latn">prayatne</i> |
| <a id="dhatu-10-0020"></a>`10.0020` | <i lang="sa-Latn">√badha~</i> | <i lang="sa-Latn">saṃyamane</i> |
| <a id="dhatu-10-0021"></a>`10.0021` | <i lang="sa-Latn">√bandha~</i> | <i lang="sa-Latn">saṃyamane</i> |
| <a id="dhatu-10-0022"></a>`10.0022` | <i lang="sa-Latn">√pṝ</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-10-0023"></a>`10.0023` | <i lang="sa-Latn">√urja~</i> | <i lang="sa-Latn">balaprāṇanayoḥ</i> |
| <a id="dhatu-10-0024"></a>`10.0024` | <i lang="sa-Latn">√pakṣa~</i> | <i lang="sa-Latn">parigrahe</i> |
| <a id="dhatu-10-0025"></a>`10.0025` | <i lang="sa-Latn">√varṇa~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-10-0026"></a>`10.0026` | <i lang="sa-Latn">√curṇa~</i> | <i lang="sa-Latn">preraṇe </i> |
| <a id="dhatu-10-0027"></a>`10.0027` | <i lang="sa-Latn">√pratha~</i> | <i lang="sa-Latn">prakhyāne</i> |
| <a id="dhatu-10-0028"></a>`10.0028` | <i lang="sa-Latn">√pṛtha~</i> | <i lang="sa-Latn">prakṣepe</i> |
| <a id="dhatu-10-0029"></a>`10.0029` | <i lang="sa-Latn">√patha~</i> | <i lang="sa-Latn">prakṣepe</i> |
| <a id="dhatu-10-0030"></a>`10.0030` | <i lang="sa-Latn">√ṣanba~</i> | <i lang="sa-Latn">sambandhane</i> |
| <a id="dhatu-10-0031"></a>`10.0031` | <i lang="sa-Latn">√śanba~</i> | <i lang="sa-Latn">sambandhane</i> |
| <a id="dhatu-10-0032"></a>`10.0032` | <i lang="sa-Latn">√sānba~</i> | <i lang="sa-Latn">sambandhane</i> |
| <a id="dhatu-10-0033"></a>`10.0033` | <i lang="sa-Latn">√bhakṣa~</i> | <i lang="sa-Latn">adane</i> |
| <a id="dhatu-10-0034"></a>`10.0034` | <i lang="sa-Latn">√kuṭṭa~</i> | <i lang="sa-Latn">chedanabhartsanayoḥ</i> |
| <a id="dhatu-10-0035"></a>`10.0035` | <i lang="sa-Latn">√puṭṭa~</i> | <i lang="sa-Latn">alpībhāve</i> |
| <a id="dhatu-10-0036"></a>`10.0036` | <i lang="sa-Latn">√cuṭṭa~</i> | <i lang="sa-Latn">alpībhāve</i> |
| <a id="dhatu-10-0037"></a>`10.0037` | <i lang="sa-Latn">√adṭa~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-10-0038"></a>`10.0038` | <i lang="sa-Latn">√ṣuṭṭa~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-10-0039"></a>`10.0039` | <i lang="sa-Latn">√lunṭa~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-10-0040"></a>`10.0040` | <i lang="sa-Latn">√lunṭha~</i> | <i lang="sa-Latn">steye</i> |
| <a id="dhatu-10-0041"></a>`10.0041` | <i lang="sa-Latn">√śaṭha~</i> | <i lang="sa-Latn">asaṃskāragatyoḥ</i> |
| <a id="dhatu-10-0042"></a>`10.0042` | <i lang="sa-Latn">√śvaṭha~</i> | <i lang="sa-Latn">asaṃskāragatyoḥ</i> |
| <a id="dhatu-10-0043"></a>`10.0043` | <i lang="sa-Latn">√śvaṭhi~</i> | <i lang="sa-Latn">asaṃskāragatyoḥ</i> |
| <a id="dhatu-10-0044"></a>`10.0044` | <i lang="sa-Latn">√tuja~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0045"></a>`10.0045` | <i lang="sa-Latn">√tuji~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0046"></a>`10.0046` | <i lang="sa-Latn">√pija~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0047"></a>`10.0047` | <i lang="sa-Latn">√piji~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0048"></a>`10.0048` | <i lang="sa-Latn">√laji~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0049"></a>`10.0049` | <i lang="sa-Latn">√luji~</i> | <i lang="sa-Latn">hiṃsābalādānaniketaneṣu</i> |
| <a id="dhatu-10-0050"></a>`10.0050` | <i lang="sa-Latn">√pisa~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0051"></a>`10.0051` | <i lang="sa-Latn">√ṣāntva~</i> | <i lang="sa-Latn">sāmaprayoge</i> |
| <a id="dhatu-10-0052"></a>`10.0052` | <i lang="sa-Latn">√sāntva~</i> | <i lang="sa-Latn">sāmaprayoge</i> |
| <a id="dhatu-10-0053"></a>`10.0053` | <i lang="sa-Latn">√śvalka~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-10-0054"></a>`10.0054` | <i lang="sa-Latn">√valka~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-10-0055"></a>`10.0055` | <i lang="sa-Latn">√ṣṇiha~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-10-0056"></a>`10.0056` | <i lang="sa-Latn">√sphiṭa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0057"></a>`10.0057` | <i lang="sa-Latn">√smiṭa~</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-10-0058"></a>`10.0058` | <i lang="sa-Latn">√ṣmiṅ</i> | <i lang="sa-Latn">anādare</i> |
| <a id="dhatu-10-0059"></a>`10.0059` | <i lang="sa-Latn">√śliṣa~</i> | <i lang="sa-Latn">śleṣaṇe</i> |
| <a id="dhatu-10-0060"></a>`10.0060` | <i lang="sa-Latn">√pathi~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0061"></a>`10.0061` | <i lang="sa-Latn">√picha~</i> | <i lang="sa-Latn">kuṭṭane</i> |
| <a id="dhatu-10-0062"></a>`10.0062` | <i lang="sa-Latn">√chadi~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-10-0063"></a>`10.0063` | <i lang="sa-Latn">√śraṇa~</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-10-0064"></a>`10.0064` | <i lang="sa-Latn">√taḍa~</i> | <i lang="sa-Latn">āghāte</i> |
| <a id="dhatu-10-0065"></a>`10.0065` | <i lang="sa-Latn">√khaḍa~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0066"></a>`10.0066` | <i lang="sa-Latn">√khaḍi~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0067"></a>`10.0067` | <i lang="sa-Latn">√kaḍi~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0068"></a>`10.0068` | <i lang="sa-Latn">√kuḍi~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-10-0069"></a>`10.0069` | <i lang="sa-Latn">√guḍi~</i> | <i lang="sa-Latn">veṣṭane</i> |
| <a id="dhatu-10-0070"></a>`10.0070` | <i lang="sa-Latn">√kuṭhi~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-10-0071"></a>`10.0071` | <i lang="sa-Latn">√guṭhi~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-10-0072"></a>`10.0072` | <i lang="sa-Latn">√khuḍi~</i> | <i lang="sa-Latn">khaṇḍane</i> |
| <a id="dhatu-10-0073"></a>`10.0073` | <i lang="sa-Latn">√vaṭi~</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-10-0074"></a>`10.0074` | <i lang="sa-Latn">√vaḍi~</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-10-0075"></a>`10.0075` | <i lang="sa-Latn">√caḍi~</i> | <i lang="sa-Latn">kope</i> |
| <a id="dhatu-10-0076"></a>`10.0076` | <i lang="sa-Latn">√maḍi~</i> | <i lang="sa-Latn">bhūṣāyāṃ harṣe ca</i> |
| <a id="dhatu-10-0077"></a>`10.0077` | <i lang="sa-Latn">√bhaḍi~</i> | <i lang="sa-Latn">kalyāṇe</i> |
| <a id="dhatu-10-0078"></a>`10.0078` | <i lang="sa-Latn">√charda~</i> | <i lang="sa-Latn">vamane</i> |
| <a id="dhatu-10-0079"></a>`10.0079` | <i lang="sa-Latn">√pusta~</i> | <i lang="sa-Latn">ādarānādarayoḥ</i> |
| <a id="dhatu-10-0080"></a>`10.0080` | <i lang="sa-Latn">√busta~</i> | <i lang="sa-Latn">ādarānādarayoḥ</i> |
| <a id="dhatu-10-0081"></a>`10.0081` | <i lang="sa-Latn">√cuda~</i> | <i lang="sa-Latn">sañcodane</i> |
| <a id="dhatu-10-0082"></a>`10.0082` | <i lang="sa-Latn">√nakka~</i> | <i lang="sa-Latn">nāśane</i> |
| <a id="dhatu-10-0083"></a>`10.0083` | <i lang="sa-Latn">√dhakka~</i> | <i lang="sa-Latn">nāśane</i> |
| <a id="dhatu-10-0084"></a>`10.0084` | <i lang="sa-Latn">√cakka~</i> | <i lang="sa-Latn">vyathane</i> |
| <a id="dhatu-10-0085"></a>`10.0085` | <i lang="sa-Latn">√cukka~</i> | <i lang="sa-Latn">vyathane</i> |
| <a id="dhatu-10-0086"></a>`10.0086` | <i lang="sa-Latn">√kṣala~</i> | <i lang="sa-Latn">śaucakarmaṇi</i> |
| <a id="dhatu-10-0087"></a>`10.0087` | <i lang="sa-Latn">√tala~</i> | <i lang="sa-Latn">pratiṣṭhāyām</i> |
| <a id="dhatu-10-0088"></a>`10.0088` | <i lang="sa-Latn">√tula~</i> | <i lang="sa-Latn">unmāne</i> |
| <a id="dhatu-10-0089"></a>`10.0089` | <i lang="sa-Latn">√dula~</i> | <i lang="sa-Latn">utkṣepe</i> |
| <a id="dhatu-10-0090"></a>`10.0090` | <i lang="sa-Latn">√pula~</i> | <i lang="sa-Latn">mahattve</i> |
| <a id="dhatu-10-0091"></a>`10.0091` | <i lang="sa-Latn">√cula~</i> | <i lang="sa-Latn">samucchrāye</i> |
| <a id="dhatu-10-0092"></a>`10.0092` | <i lang="sa-Latn">√mūla~</i> | <i lang="sa-Latn">rohaṇe</i> |
| <a id="dhatu-10-0093"></a>`10.0093` | <i lang="sa-Latn">√kala~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0094"></a>`10.0094` | <i lang="sa-Latn">√vila~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0095"></a>`10.0095` | <i lang="sa-Latn">√bila~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0096"></a>`10.0096` | <i lang="sa-Latn">√tila~</i> | <i lang="sa-Latn">snehane</i> |
| <a id="dhatu-10-0097"></a>`10.0097` | <i lang="sa-Latn">√cala~</i> | <i lang="sa-Latn">bhṛtau</i> |
| <a id="dhatu-10-0098"></a>`10.0098` | <i lang="sa-Latn">√pāla~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-10-0099"></a>`10.0099` | <i lang="sa-Latn">√pala~</i> | <i lang="sa-Latn">rakṣaṇe</i> |
| <a id="dhatu-10-0100"></a>`10.0100` | <i lang="sa-Latn">√lūṣa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0101"></a>`10.0101` | <i lang="sa-Latn">√śulba~</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-10-0102"></a>`10.0102` | <i lang="sa-Latn">√śūrpa~</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-10-0103"></a>`10.0103` | <i lang="sa-Latn">√cuṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-10-0104"></a>`10.0104` | <i lang="sa-Latn">√muṭa~</i> | <i lang="sa-Latn">sañcūrṇane</i> |
| <a id="dhatu-10-0105"></a>`10.0105` | <i lang="sa-Latn">√ulaḍi~</i> | <i lang="sa-Latn">utkṣepaṇe</i> |
| <a id="dhatu-10-0106"></a>`10.0106` | <i lang="sa-Latn">√paḍi~</i> | <i lang="sa-Latn">nāśane</i> |
| <a id="dhatu-10-0107"></a>`10.0107` | <i lang="sa-Latn">√pasi~</i> | <i lang="sa-Latn">nāśane</i> |
| <a id="dhatu-10-0108"></a>`10.0108` | <i lang="sa-Latn">√mārga</i> | <i lang="sa-Latn">saṃskāragatyoḥ</i> |
| <a id="dhatu-10-0109"></a>`10.0109` | <i lang="sa-Latn">√vraja~</i> | <i lang="sa-Latn">saṃskāragatyoḥ</i> |
| <a id="dhatu-10-0110"></a>`10.0110` | <i lang="sa-Latn">√śulka~</i> | <i lang="sa-Latn">atisparśane</i> |
| <a id="dhatu-10-0111"></a>`10.0111` | <i lang="sa-Latn">√capi~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-10-0112"></a>`10.0112` | <i lang="sa-Latn">√kṣapi~</i> | <i lang="sa-Latn">kṣāntyām</i> |
| <a id="dhatu-10-0113"></a>`10.0113` | <i lang="sa-Latn">√kṣaji~</i> | <i lang="sa-Latn">kṛcchrajīvane</i> |
| <a id="dhatu-10-0114"></a>`10.0114` | <i lang="sa-Latn">√chaji~</i> | <i lang="sa-Latn">kṛcchrajīvane</i> |
| <a id="dhatu-10-0115"></a>`10.0115` | <i lang="sa-Latn">√śvarta~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-10-0116"></a>`10.0116` | <i lang="sa-Latn">√svarta~</i> | <i lang="sa-Latn">kṛcchrajīvane, gatyām</i> |
| <a id="dhatu-10-0117"></a>`10.0117` | <i lang="sa-Latn">√śvabhra~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-10-0118"></a>`10.0118` | <i lang="sa-Latn">√jñapa~</i> | <i lang="sa-Latn">jñāne jñāpane ca</i> |
| <a id="dhatu-10-0119"></a>`10.0119` | <i lang="sa-Latn">√yama~</i> | <i lang="sa-Latn">pariveṣaṇe</i> |
| <a id="dhatu-10-0120"></a>`10.0120` | <i lang="sa-Latn">√caha~</i> | <i lang="sa-Latn">parikalkane</i> |
| <a id="dhatu-10-0121"></a>`10.0121` | <i lang="sa-Latn">√capa~</i> | <i lang="sa-Latn">parikalpane</i> |
| <a id="dhatu-10-0122"></a>`10.0122` | <i lang="sa-Latn">√raha~</i> | <i lang="sa-Latn">tyāge</i> |
| <a id="dhatu-10-0123"></a>`10.0123` | <i lang="sa-Latn">√bala~</i> | <i lang="sa-Latn">prāṇane</i> |
| <a id="dhatu-10-0124"></a>`10.0124` | <i lang="sa-Latn">√ciñ</i> | <i lang="sa-Latn">cayane</i> |
| <a id="dhatu-10-0125"></a>`10.0125` | <i lang="sa-Latn">√ghaṭṭa~</i> | <i lang="sa-Latn">calane</i> |
| <a id="dhatu-10-0126"></a>`10.0126` | <i lang="sa-Latn">√musta~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0127"></a>`10.0127` | <i lang="sa-Latn">√khaṭṭa~</i> | <i lang="sa-Latn">saṃvaraṇe</i> |
| <a id="dhatu-10-0128"></a>`10.0128` | <i lang="sa-Latn">√ṣaṭṭa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0129"></a>`10.0129` | <i lang="sa-Latn">√sphiṭṭa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0130"></a>`10.0130` | <i lang="sa-Latn">√cubi~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0131"></a>`10.0131` | <i lang="sa-Latn">√pula~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0132"></a>`10.0132` | <i lang="sa-Latn">√pūrṇa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0133"></a>`10.0133` | <i lang="sa-Latn">√puṇa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0134"></a>`10.0134` | <i lang="sa-Latn">√punsa~</i> | <i lang="sa-Latn">abhivardhane</i> |
| <a id="dhatu-10-0135"></a>`10.0135` | <i lang="sa-Latn">√ṭaki~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-10-0136"></a>`10.0136` | <i lang="sa-Latn">√vyapa~</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-10-0137"></a>`10.0137` | <i lang="sa-Latn">√vyaya~</i> | <i lang="sa-Latn">kṣaye</i> |
| <a id="dhatu-10-0138"></a>`10.0138` | <i lang="sa-Latn">√pūla~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0139"></a>`10.0139` | <i lang="sa-Latn">√dhūsa~</i> | <i lang="sa-Latn">kāntikaraṇe</i> |
| <a id="dhatu-10-0140"></a>`10.0140` | <i lang="sa-Latn">√dhūṣa~</i> | <i lang="sa-Latn">kāntikaraṇe</i> |
| <a id="dhatu-10-0141"></a>`10.0141` | <i lang="sa-Latn">√dhūśa~</i> | <i lang="sa-Latn">kāntikaraṇe</i> |
| <a id="dhatu-10-0142"></a>`10.0142` | <i lang="sa-Latn">√kīṭa~</i> | <i lang="sa-Latn">varṇe</i> |
| <a id="dhatu-10-0143"></a>`10.0143` | <i lang="sa-Latn">√cūrṇa~</i> | <i lang="sa-Latn">saṅkocane</i> |
| <a id="dhatu-10-0144"></a>`10.0144` | <i lang="sa-Latn">√pūja~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0145"></a>`10.0145` | <i lang="sa-Latn">√arka~</i> | <i lang="sa-Latn">stavane</i> |
| <a id="dhatu-10-0146"></a>`10.0146` | <i lang="sa-Latn">√śuṭha~</i> | <i lang="sa-Latn">ālasye</i> |
| <a id="dhatu-10-0147"></a>`10.0147` | <i lang="sa-Latn">√śuṭhi~</i> | <i lang="sa-Latn">śoṣaṇe</i> |
| <a id="dhatu-10-0148"></a>`10.0148` | <i lang="sa-Latn">√juḍa~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-10-0149"></a>`10.0149` | <i lang="sa-Latn">√gaja~</i> | <i lang="sa-Latn">śabdārthe</i> |
| <a id="dhatu-10-0150"></a>`10.0150` | <i lang="sa-Latn">√mārja~</i> | <i lang="sa-Latn">śabdārthe</i> |
| <a id="dhatu-10-0151"></a>`10.0151` | <i lang="sa-Latn">√marca~</i> | <i lang="sa-Latn">śabdārthe</i> |
| <a id="dhatu-10-0152"></a>`10.0152` | <i lang="sa-Latn">√ghṛ</i> | <i lang="sa-Latn">prasravaṇe</i> |
| <a id="dhatu-10-0153"></a>`10.0153` | <i lang="sa-Latn">√paci~</i> | <i lang="sa-Latn">vistāravacane</i> |
| <a id="dhatu-10-0154"></a>`10.0154` | <i lang="sa-Latn">√tija~</i> | <i lang="sa-Latn">niśāne</i> |
| <a id="dhatu-10-0155"></a>`10.0155` | <i lang="sa-Latn">√kṝta~</i> | <i lang="sa-Latn">saṃśabdane</i> |
| <a id="dhatu-10-0156"></a>`10.0156` | <i lang="sa-Latn">√vardha~</i> | <i lang="sa-Latn">chedanapūraṇayoḥ</i> |
| <a id="dhatu-10-0157"></a>`10.0157` | <i lang="sa-Latn">√kubi~</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-10-0158"></a>`10.0158` | <i lang="sa-Latn">√kubhi~</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-10-0159"></a>`10.0159` | <i lang="sa-Latn">√lubi~</i> | <i lang="sa-Latn">adarśane</i> |
| <a id="dhatu-10-0160"></a>`10.0160` | <i lang="sa-Latn">√tubi~</i> | <i lang="sa-Latn">adarśane</i> |
| <a id="dhatu-10-0161"></a>`10.0161` | <i lang="sa-Latn">√hlapa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-10-0162"></a>`10.0162` | <i lang="sa-Latn">√klapa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-10-0163"></a>`10.0163` | <i lang="sa-Latn">√hrapa~</i> | <i lang="sa-Latn">vyaktāyāṃ vāci</i> |
| <a id="dhatu-10-0164"></a>`10.0164` | <i lang="sa-Latn">√cuṭi~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-10-0165"></a>`10.0165` | <i lang="sa-Latn">√brīsa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0166"></a>`10.0166` | <i lang="sa-Latn">√dahi~</i> | <i lang="sa-Latn">rakṣaṇe mokṣaṇe ca</i> |
| <a id="dhatu-10-0167"></a>`10.0167` | <i lang="sa-Latn">√ila~</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-10-0168"></a>`10.0168` | <i lang="sa-Latn">√mrakṣa~</i> | <i lang="sa-Latn">mlecchane</i> |
| <a id="dhatu-10-0169"></a>`10.0169` | <i lang="sa-Latn">√asta~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0170"></a>`10.0170` | <i lang="sa-Latn">√mlecha~</i> | <i lang="sa-Latn">avyaktāyāṃ vāci</i> |
| <a id="dhatu-10-0171"></a>`10.0171` | <i lang="sa-Latn">√chapi~</i> | <i lang="sa-Latn">gatyām</i> |
| <a id="dhatu-10-0172"></a>`10.0172` | <i lang="sa-Latn">√brūsa~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0173"></a>`10.0173` | <i lang="sa-Latn">√barha~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0174"></a>`10.0174` | <i lang="sa-Latn">√śraṇu~</i> | <i lang="sa-Latn">dāne</i> |
| <a id="dhatu-10-0175"></a>`10.0175` | <i lang="sa-Latn">√picca~</i> | <i lang="sa-Latn">kuṭṭane</i> |
| <a id="dhatu-10-0176"></a>`10.0176` | <i lang="sa-Latn">√bula~</i> | <i lang="sa-Latn">nimajjane</i> |
| <a id="dhatu-10-0177"></a>`10.0177` | <i lang="sa-Latn">√garja~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-10-0178"></a>`10.0178` | <i lang="sa-Latn">√garda~</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-10-0179"></a>`10.0179` | <i lang="sa-Latn">√gardha~</i> | <i lang="sa-Latn">abhikāṅkṣāyām</i> |
| <a id="dhatu-10-0180"></a>`10.0180` | <i lang="sa-Latn">√gurda~</i> | <i lang="sa-Latn">pūrvaniketane</i> |
| <a id="dhatu-10-0181"></a>`10.0181` | <i lang="sa-Latn">√pūrva~</i> | <i lang="sa-Latn">niketane</i> |
| <a id="dhatu-10-0182"></a>`10.0182` | <i lang="sa-Latn">√jasi~</i> | <i lang="sa-Latn">rakṣaṇe mokṣaṇe ca</i> |
| <a id="dhatu-10-0183"></a>`10.0183` | <i lang="sa-Latn">√īḍa~</i> | <i lang="sa-Latn">stutau</i> |
| <a id="dhatu-10-0184"></a>`10.0184` | <i lang="sa-Latn">√jasu~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0185"></a>`10.0185` | <i lang="sa-Latn">√piḍi~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0186"></a>`10.0186` | <i lang="sa-Latn">√partha~</i> | <i lang="sa-Latn">prakṣepe</i> |
| <a id="dhatu-10-0187"></a>`10.0187` | <i lang="sa-Latn">√ruṣa~</i> | <i lang="sa-Latn">roṣe</i> |
| <a id="dhatu-10-0188"></a>`10.0188` | <i lang="sa-Latn">√ruṭa~</i> | <i lang="sa-Latn">roṣe</i> |
| <a id="dhatu-10-0189"></a>`10.0189` | <i lang="sa-Latn">√ḍipa~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0190"></a>`10.0190` | <i lang="sa-Latn">√ṣṭupa~</i> | <i lang="sa-Latn">samucchrāye</i> |
| <a id="dhatu-10-0191"></a>`10.0191` | <i lang="sa-Latn">√ṣṭūpa~</i> | <i lang="sa-Latn">samucchrāye</i> |
| <a id="dhatu-10-0192"></a>`10.0192` | <i lang="sa-Latn">√cita~</i> | <i lang="sa-Latn">sañcetane</i> |
| <a id="dhatu-10-0193"></a>`10.0193` | <i lang="sa-Latn">√daśi~</i> | <i lang="sa-Latn">daṃśane</i> |
| <a id="dhatu-10-0194"></a>`10.0194` | <i lang="sa-Latn">√dasi~</i> | <i lang="sa-Latn">darśanadaṃśanayoḥ</i> |
| <a id="dhatu-10-0195"></a>`10.0195` | <i lang="sa-Latn">√dasa~</i> | <i lang="sa-Latn">darśanadaṃśanayoḥ</i> |
| <a id="dhatu-10-0196"></a>`10.0196` | <i lang="sa-Latn">√ḍapa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0197"></a>`10.0197` | <i lang="sa-Latn">√ḍipa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0198"></a>`10.0198` | <i lang="sa-Latn">√tatri~</i> | <i lang="sa-Latn">kuṭumbadhāraṇe</i> |
| <a id="dhatu-10-0199"></a>`10.0199` | <i lang="sa-Latn">√matri~</i> | <i lang="sa-Latn">guptaparibhāṣaṇe</i> |
| <a id="dhatu-10-0200"></a>`10.0200` | <i lang="sa-Latn">√spaśa~</i> | <i lang="sa-Latn">grahaṇasaṃśleṣaṇayoḥ</i> |
| <a id="dhatu-10-0201"></a>`10.0201` | <i lang="sa-Latn">√tarja~</i> | <i lang="sa-Latn">tarjane</i> |
| <a id="dhatu-10-0202"></a>`10.0202` | <i lang="sa-Latn">√bhartsa~</i> | <i lang="sa-Latn">tarjane</i> |
| <a id="dhatu-10-0203"></a>`10.0203` | <i lang="sa-Latn">√basta~</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-10-0204"></a>`10.0204` | <i lang="sa-Latn">√gandha~</i> | <i lang="sa-Latn">ardane</i> |
| <a id="dhatu-10-0205"></a>`10.0205` | <i lang="sa-Latn">√kila~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0206"></a>`10.0206` | <i lang="sa-Latn">√pila~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0207"></a>`10.0207` | <i lang="sa-Latn">√viṣka~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0208"></a>`10.0208` | <i lang="sa-Latn">√hiṣka~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0209"></a>`10.0209` | <i lang="sa-Latn">√niṣka~</i> | <i lang="sa-Latn">parimāṇe</i> |
| <a id="dhatu-10-0210"></a>`10.0210` | <i lang="sa-Latn">√lala~</i> | <i lang="sa-Latn">īpsāyām</i> |
| <a id="dhatu-10-0211"></a>`10.0211` | <i lang="sa-Latn">√kūṇa~</i> | <i lang="sa-Latn">saṅkoce</i> |
| <a id="dhatu-10-0212"></a>`10.0212` | <i lang="sa-Latn">√tūṇa~</i> | <i lang="sa-Latn">pūraṇe</i> |
| <a id="dhatu-10-0213"></a>`10.0213` | <i lang="sa-Latn">√bhrūṇa~</i> | <i lang="sa-Latn">āśāviśaṅkayoḥ</i> |
| <a id="dhatu-10-0214"></a>`10.0214` | <i lang="sa-Latn">√śaṭha~</i> | <i lang="sa-Latn">ślāghāyām</i> |
| <a id="dhatu-10-0215"></a>`10.0215` | <i lang="sa-Latn">√yakṣa~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0216"></a>`10.0216` | <i lang="sa-Latn">√syama~</i> | <i lang="sa-Latn">vitarke</i> |
| <a id="dhatu-10-0217"></a>`10.0217` | <i lang="sa-Latn">√gūra~</i> | <i lang="sa-Latn">udyamane</i> |
| <a id="dhatu-10-0218"></a>`10.0218` | <i lang="sa-Latn">√śama~</i> | <i lang="sa-Latn">ālocane</i> |
| <a id="dhatu-10-0219"></a>`10.0219` | <i lang="sa-Latn">√lakṣa~</i> | <i lang="sa-Latn">ālocane</i> |
| <a id="dhatu-10-0220"></a>`10.0220` | <i lang="sa-Latn">√kutsa~</i> | <i lang="sa-Latn">avakṣepaṇe nindane ca</i> |
| <a id="dhatu-10-0221"></a>`10.0221` | <i lang="sa-Latn">√truṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-10-0222"></a>`10.0222` | <i lang="sa-Latn">√kuṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-10-0223"></a>`10.0223` | <i lang="sa-Latn">√gala~</i> | <i lang="sa-Latn">sravaṇe</i> |
| <a id="dhatu-10-0224"></a>`10.0224` | <i lang="sa-Latn">√bhala~</i> | <i lang="sa-Latn">ābhaṇḍane</i> |
| <a id="dhatu-10-0225"></a>`10.0225` | <i lang="sa-Latn">√kūṭa~</i> | <i lang="sa-Latn">āpradāne avasādane ca</i> |
| <a id="dhatu-10-0226"></a>`10.0226` | <i lang="sa-Latn">√kuṭṭa~</i> | <i lang="sa-Latn">pratāpane</i> |
| <a id="dhatu-10-0227"></a>`10.0227` | <i lang="sa-Latn">√vancu~</i> | <i lang="sa-Latn">pralambhane</i> |
| <a id="dhatu-10-0228"></a>`10.0228` | <i lang="sa-Latn">√vṛṣa~</i> | <i lang="sa-Latn">śaktibandhane</i> |
| <a id="dhatu-10-0229"></a>`10.0229` | <i lang="sa-Latn">√mada~</i> | <i lang="sa-Latn">tṛptiyoge</i> |
| <a id="dhatu-10-0230"></a>`10.0230` | <i lang="sa-Latn">√divu~</i> | <i lang="sa-Latn">parikūjane</i> |
| <a id="dhatu-10-0231"></a>`10.0231` | <i lang="sa-Latn">√gṛ</i> | <i lang="sa-Latn">vijñāne</i> |
| <a id="dhatu-10-0232"></a>`10.0232` | <i lang="sa-Latn">√vida~</i> | <i lang="sa-Latn">cetanākhyānanivāseṣu</i> |
| <a id="dhatu-10-0233"></a>`10.0233` | <i lang="sa-Latn">√māna~</i> | <i lang="sa-Latn">stambhe</i> |
| <a id="dhatu-10-0234"></a>`10.0234` | <i lang="sa-Latn">√mana~</i> | <i lang="sa-Latn">stambhe</i> |
| <a id="dhatu-10-0235"></a>`10.0235` | <i lang="sa-Latn">√yu</i> | <i lang="sa-Latn">jugupsāyām</i> |
| <a id="dhatu-10-0236"></a>`10.0236` | <i lang="sa-Latn">√kusma~</i> | <i lang="sa-Latn">kutsitasmaye</i> |
| <a id="dhatu-10-0237"></a>`10.0237` | <i lang="sa-Latn">√carca~</i> | <i lang="sa-Latn">adhyayane</i> |
| <a id="dhatu-10-0238"></a>`10.0238` | <i lang="sa-Latn">√bukka~</i> | <i lang="sa-Latn">bhaṣaṇe</i> |
| <a id="dhatu-10-0239"></a>`10.0239` | <i lang="sa-Latn">√śabda~</i> | <i lang="sa-Latn">āviṣkāre, bhaṣaṇe</i> |
| <a id="dhatu-10-0240"></a>`10.0240` | <i lang="sa-Latn">√kaṇa~</i> | <i lang="sa-Latn">nimīlane</i> |
| <a id="dhatu-10-0241"></a>`10.0241` | <i lang="sa-Latn">√jabhi~</i> | <i lang="sa-Latn">nāśane</i> |
| <a id="dhatu-10-0242"></a>`10.0242` | <i lang="sa-Latn">√ṣūda~</i> | <i lang="sa-Latn">kṣaraṇe āsravaṇe āpravaṇe ghāte ca</i> |
| <a id="dhatu-10-0243"></a>`10.0243` | <i lang="sa-Latn">√jasu~</i> | <i lang="sa-Latn">tāḍane</i> |
| <a id="dhatu-10-0244"></a>`10.0244` | <i lang="sa-Latn">√paśa~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-10-0245"></a>`10.0245` | <i lang="sa-Latn">√ama~</i> | <i lang="sa-Latn">roge</i> |
| <a id="dhatu-10-0246"></a>`10.0246` | <i lang="sa-Latn">√caṭa~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0247"></a>`10.0247` | <i lang="sa-Latn">√sphuṭa~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0248"></a>`10.0248` | <i lang="sa-Latn">√ghaṭa~</i> | <i lang="sa-Latn">saṅghāte</i> |
| <a id="dhatu-10-0249"></a>`10.0249` | <i lang="sa-Latn">√divu~</i> | <i lang="sa-Latn">mardane</i> |
| <a id="dhatu-10-0250"></a>`10.0250` | <i lang="sa-Latn">√arja~</i> | <i lang="sa-Latn">pratiyatne</i> |
| <a id="dhatu-10-0251"></a>`10.0251` | <i lang="sa-Latn">√ghuṣi~r</i> | <i lang="sa-Latn">viśabdane</i> |
| <a id="dhatu-10-0252"></a>`10.0252` | <i lang="sa-Latn">√kranda~</i> | <i lang="sa-Latn">sātatye</i> |
| <a id="dhatu-10-0253"></a>`10.0253` | <i lang="sa-Latn">√lasa~</i> | <i lang="sa-Latn">śilpayoge</i> |
| <a id="dhatu-10-0254"></a>`10.0254` | <i lang="sa-Latn">√tasi~</i> | <i lang="sa-Latn">alaṅkaraṇe</i> |
| <a id="dhatu-10-0255"></a>`10.0255` | <i lang="sa-Latn">√bhūṣa~</i> | <i lang="sa-Latn">alaṅkaraṇe</i> |
| <a id="dhatu-10-0256"></a>`10.0256` | <i lang="sa-Latn">√mokṣa~</i> | <i lang="sa-Latn">mocane</i> |
| <a id="dhatu-10-0257"></a>`10.0257` | <i lang="sa-Latn">√arha~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0258"></a>`10.0258` | <i lang="sa-Latn">√jñā</i> | <i lang="sa-Latn">niyoge</i> |
| <a id="dhatu-10-0259"></a>`10.0259` | <i lang="sa-Latn">√bhaja~</i> | <i lang="sa-Latn">viśrāṇane</i> |
| <a id="dhatu-10-0260"></a>`10.0260` | <i lang="sa-Latn">√śṛdhu~</i> | <i lang="sa-Latn">prahasane prasahane ca</i> |
| <a id="dhatu-10-0261"></a>`10.0261` | <i lang="sa-Latn">√yata~</i> | <i lang="sa-Latn">nikāropaskārayoḥ</i> |
| <a id="dhatu-10-0262"></a>`10.0262` | <i lang="sa-Latn">√raka~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0263"></a>`10.0263` | <i lang="sa-Latn">√laga~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0264"></a>`10.0264` | <i lang="sa-Latn">√ragha~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0265"></a>`10.0265` | <i lang="sa-Latn">√raga~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0266"></a>`10.0266` | <i lang="sa-Latn">√ancu~</i> | <i lang="sa-Latn">viśeṣaṇe</i> |
| <a id="dhatu-10-0267"></a>`10.0267` | <i lang="sa-Latn">√ligi~</i> | <i lang="sa-Latn">citrīkaraṇe</i> |
| <a id="dhatu-10-0268"></a>`10.0268` | <i lang="sa-Latn">√muda~</i> | <i lang="sa-Latn">saṃsarge</i> |
| <a id="dhatu-10-0269"></a>`10.0269` | <i lang="sa-Latn">√trasa~</i> | <i lang="sa-Latn">dhāraṇe grahaṇe vāraṇe ca</i> |
| <a id="dhatu-10-0270"></a>`10.0270` | <i lang="sa-Latn">√u~dhrasa~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-10-0271"></a>`10.0271` | <i lang="sa-Latn">√udhrasa~</i> | <i lang="sa-Latn">uñche</i> |
| <a id="dhatu-10-0272"></a>`10.0272` | <i lang="sa-Latn">√muca~</i> | <i lang="sa-Latn">pramocane modane ca</i> |
| <a id="dhatu-10-0273"></a>`10.0273` | <i lang="sa-Latn">√vasa~</i> | <i lang="sa-Latn">snehacchedāpaharaṇeṣu</i> |
| <a id="dhatu-10-0274"></a>`10.0274` | <i lang="sa-Latn">√cara~</i> | <i lang="sa-Latn">saṃśaye</i> |
| <a id="dhatu-10-0275"></a>`10.0275` | <i lang="sa-Latn">√cyu</i> | <i lang="sa-Latn">sahane hasane ca</i> |
| <a id="dhatu-10-0276"></a>`10.0276` | <i lang="sa-Latn">√cyusa~</i> | <i lang="sa-Latn">sahane hasane ca</i> |
| <a id="dhatu-10-0277"></a>`10.0277` | <i lang="sa-Latn">√bhū</i> | <i lang="sa-Latn">avakalkane</i> |
| <a id="dhatu-10-0278"></a>`10.0278` | <i lang="sa-Latn">√kṛpa~</i> | <i lang="sa-Latn">avakalkane</i> |
| <a id="dhatu-10-0279"></a>`10.0279` | <i lang="sa-Latn">√grasa~</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-10-0280"></a>`10.0280` | <i lang="sa-Latn">√puṣa~</i> | <i lang="sa-Latn">dhāraṇe</i> |
| <a id="dhatu-10-0281"></a>`10.0281` | <i lang="sa-Latn">√dala~</i> | <i lang="sa-Latn">vidāraṇe</i> |
| <a id="dhatu-10-0282"></a>`10.0282` | <i lang="sa-Latn">√paṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0283"></a>`10.0283` | <i lang="sa-Latn">√puṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0284"></a>`10.0284` | <i lang="sa-Latn">√luṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0285"></a>`10.0285` | <i lang="sa-Latn">√tuji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0286"></a>`10.0286` | <i lang="sa-Latn">√miji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0287"></a>`10.0287` | <i lang="sa-Latn">√piji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0288"></a>`10.0288` | <i lang="sa-Latn">√laka~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0289"></a>`10.0289` | <i lang="sa-Latn">√luji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0290"></a>`10.0290` | <i lang="sa-Latn">√bhaji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0291"></a>`10.0291` | <i lang="sa-Latn">√laghi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0292"></a>`10.0292` | <i lang="sa-Latn">√trasi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0293"></a>`10.0293` | <i lang="sa-Latn">√pisi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0294"></a>`10.0294` | <i lang="sa-Latn">√kusi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0295"></a>`10.0295` | <i lang="sa-Latn">√daśi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0296"></a>`10.0296` | <i lang="sa-Latn">√kuśi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0297"></a>`10.0297` | <i lang="sa-Latn">√ghaṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0298"></a>`10.0298` | <i lang="sa-Latn">√ghaṭi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0299"></a>`10.0299` | <i lang="sa-Latn">√bṛhi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0300"></a>`10.0300` | <i lang="sa-Latn">√barha~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0301"></a>`10.0301` | <i lang="sa-Latn">√balha~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0302"></a>`10.0302` | <i lang="sa-Latn">√gupa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0303"></a>`10.0303` | <i lang="sa-Latn">√dhūpa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0304"></a>`10.0304` | <i lang="sa-Latn">√vicha~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0305"></a>`10.0305` | <i lang="sa-Latn">√cīva~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0306"></a>`10.0306` | <i lang="sa-Latn">√putha~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0307"></a>`10.0307` | <i lang="sa-Latn">√lokṛ~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0308"></a>`10.0308` | <i lang="sa-Latn">√locṛ~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0309"></a>`10.0309` | <i lang="sa-Latn">√ṇada~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0310"></a>`10.0310` | <i lang="sa-Latn">√kupa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0311"></a>`10.0311` | <i lang="sa-Latn">√tarka~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0312"></a>`10.0312` | <i lang="sa-Latn">√vṛtu~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0313"></a>`10.0313` | <i lang="sa-Latn">√vṛdhu~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0314"></a>`10.0314` | <i lang="sa-Latn">√ruṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0315"></a>`10.0315` | <i lang="sa-Latn">√laji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0316"></a>`10.0316` | <i lang="sa-Latn">√aji~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0317"></a>`10.0317` | <i lang="sa-Latn">√dasi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0318"></a>`10.0318` | <i lang="sa-Latn">√bhṛśi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0319"></a>`10.0319` | <i lang="sa-Latn">√ruśi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0320"></a>`10.0320` | <i lang="sa-Latn">√śīka~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0321"></a>`10.0321` | <i lang="sa-Latn">√rusi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0322"></a>`10.0322` | <i lang="sa-Latn">√naṭi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0323"></a>`10.0323` | <i lang="sa-Latn">√puṭi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0324"></a>`10.0324` | <i lang="sa-Latn">√ji</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0325"></a>`10.0325` | <i lang="sa-Latn">√ci</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0326"></a>`10.0326` | <i lang="sa-Latn">√radhi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0327"></a>`10.0327` | <i lang="sa-Latn">√laghi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0328"></a>`10.0328` | <i lang="sa-Latn">√ahi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0329"></a>`10.0329` | <i lang="sa-Latn">√rahi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0330"></a>`10.0330` | <i lang="sa-Latn">√mahi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0331"></a>`10.0331` | <i lang="sa-Latn">√laḍi~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0332"></a>`10.0332` | <i lang="sa-Latn">√taḍa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0333"></a>`10.0333` | <i lang="sa-Latn">√nala~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0334"></a>`10.0334` | <i lang="sa-Latn">√pūrī~</i> | <i lang="sa-Latn">āpyāyane</i> |
| <a id="dhatu-10-0335"></a>`10.0335` | <i lang="sa-Latn">√ruja~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0336"></a>`10.0336` | <i lang="sa-Latn">√ṣvada~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0337"></a>`10.0337` | <i lang="sa-Latn">√svāda~</i> | <i lang="sa-Latn">āsvādane</i> |
| <a id="dhatu-10-0338"></a>`10.0338` | <i lang="sa-Latn">√yu\ja~</i> | <i lang="sa-Latn">saṃyamane</i> |
| <a id="dhatu-10-0339"></a>`10.0339` | <i lang="sa-Latn">√pṛca~</i> | <i lang="sa-Latn">saṃyamane</i> |
| <a id="dhatu-10-0340"></a>`10.0340` | <i lang="sa-Latn">√arca~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0341"></a>`10.0341` | <i lang="sa-Latn">√ṣaha~</i> | <i lang="sa-Latn">marṣaṇe</i> |
| <a id="dhatu-10-0342"></a>`10.0342` | <i lang="sa-Latn">√īra~</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0343"></a>`10.0343` | <i lang="sa-Latn">√lī</i> | <i lang="sa-Latn">dravīkaraṇe</i> |
| <a id="dhatu-10-0344"></a>`10.0344` | <i lang="sa-Latn">√vṛjī~</i> | <i lang="sa-Latn">varjane</i> |
| <a id="dhatu-10-0345"></a>`10.0345` | <i lang="sa-Latn">√vṛñ</i> | <i lang="sa-Latn">āvaraṇe</i> |
| <a id="dhatu-10-0346"></a>`10.0346` | <i lang="sa-Latn">√jṝ</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-10-0347"></a>`10.0347` | <i lang="sa-Latn">√jri\</i> | <i lang="sa-Latn">vayohānau</i> |
| <a id="dhatu-10-0348"></a>`10.0348` | <i lang="sa-Latn">√ri\ca~</i> | <i lang="sa-Latn">viyojanasamparcanayoḥ</i> |
| <a id="dhatu-10-0349"></a>`10.0349` | <i lang="sa-Latn">√śi\ṣa~</i> | <i lang="sa-Latn">asarvopayoge</i> |
| <a id="dhatu-10-0350"></a>`10.0350` | <i lang="sa-Latn">√ta\pa~</i> | <i lang="sa-Latn">dāhe</i> |
| <a id="dhatu-10-0351"></a>`10.0351` | <i lang="sa-Latn">√tṛpa~</i> | <i lang="sa-Latn">tṛptau sandīpane prīṇane ca</i> |
| <a id="dhatu-10-0352"></a>`10.0352` | <i lang="sa-Latn">√chṛdī~</i> | <i lang="sa-Latn">sandīpane</i> |
| <a id="dhatu-10-0353"></a>`10.0353` | <i lang="sa-Latn">√cṛpa~</i> | <i lang="sa-Latn">sandīpane</i> |
| <a id="dhatu-10-0354"></a>`10.0354` | <i lang="sa-Latn">√chṛpa~</i> | <i lang="sa-Latn">sandīpane</i> |
| <a id="dhatu-10-0355"></a>`10.0355` | <i lang="sa-Latn">√tṛpa~</i> | <i lang="sa-Latn">dīpane sandīpane</i> |
| <a id="dhatu-10-0356"></a>`10.0356` | <i lang="sa-Latn">√dṛpa~</i> | <i lang="sa-Latn">sandīpane</i> |
| <a id="dhatu-10-0357"></a>`10.0357` | <i lang="sa-Latn">√dṛbhī~</i> | <i lang="sa-Latn">bhaye</i> |
| <a id="dhatu-10-0358"></a>`10.0358` | <i lang="sa-Latn">√dṛbha~</i> | <i lang="sa-Latn">sandarbhe</i> |
| <a id="dhatu-10-0359"></a>`10.0359` | <i lang="sa-Latn">√laṭa~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0360"></a>`10.0360` | <i lang="sa-Latn">√śratha~</i> | <i lang="sa-Latn">mokṣaṇe hiṃsāyāṃ ca</i> |
| <a id="dhatu-10-0361"></a>`10.0361` | <i lang="sa-Latn">√mī\</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0362"></a>`10.0362` | <i lang="sa-Latn">√grantha~</i> | <i lang="sa-Latn">bandhane</i> |
| <a id="dhatu-10-0363"></a>`10.0363` | <i lang="sa-Latn">√śīka~</i> | <i lang="sa-Latn">āmarṣaṇe</i> |
| <a id="dhatu-10-0364"></a>`10.0364` | <i lang="sa-Latn">√cīka~</i> | <i lang="sa-Latn">āmarṣaṇe</i> |
| <a id="dhatu-10-0365"></a>`10.0365` | <i lang="sa-Latn">√arda~^</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0366"></a>`10.0366` | <i lang="sa-Latn">√hisi~</i> | <i lang="sa-Latn">hiṃsāyām</i> |
| <a id="dhatu-10-0367"></a>`10.0367` | <i lang="sa-Latn">√arha~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0368"></a>`10.0368` | <i lang="sa-Latn">√ṣa\da~</i> | <i lang="sa-Latn">padyarthe</i> |
| <a id="dhatu-10-0369"></a>`10.0369` | <i lang="sa-Latn">√śundha~</i> | <i lang="sa-Latn">śaucakarmaṇi</i> |
| <a id="dhatu-10-0370"></a>`10.0370` | <i lang="sa-Latn">√chada~</i> | <i lang="sa-Latn">apavāraṇe</i> |
| <a id="dhatu-10-0371"></a>`10.0371` | <i lang="sa-Latn">√juṣa~</i> | <i lang="sa-Latn">paritarkaṇe paritarpaṇe ca</i> |
| <a id="dhatu-10-0372"></a>`10.0372` | <i lang="sa-Latn">√dhūñ</i> | <i lang="sa-Latn">kampane</i> |
| <a id="dhatu-10-0373"></a>`10.0373` | <i lang="sa-Latn">√prīñ</i> | <i lang="sa-Latn">tarpaṇe kāntau ca</i> |
| <a id="dhatu-10-0374"></a>`10.0374` | <i lang="sa-Latn">√śrantha~</i> | <i lang="sa-Latn">sandarbhe</i> |
| <a id="dhatu-10-0375"></a>`10.0375` | <i lang="sa-Latn">√grantha~</i> | <i lang="sa-Latn">sandarbhe</i> |
| <a id="dhatu-10-0376"></a>`10.0376` | <i lang="sa-Latn">√āpḷ~</i> | <i lang="sa-Latn">lambhane</i> |
| <a id="dhatu-10-0377"></a>`10.0377` | <i lang="sa-Latn">√tanu~</i> | <i lang="sa-Latn">śraddhopakaraṇayoḥ</i> |
| <a id="dhatu-10-0378"></a>`10.0378` | <i lang="sa-Latn">√cana~</i> | <i lang="sa-Latn">śraddhopahananayoḥ</i> |
| <a id="dhatu-10-0379"></a>`10.0379` | <i lang="sa-Latn">√vada~^</i> | <i lang="sa-Latn">sandeśavacane</i> |
| <a id="dhatu-10-0380"></a>`10.0380` | <i lang="sa-Latn">√va\ca~</i> | <i lang="sa-Latn">paribhāṣaṇe</i> |
| <a id="dhatu-10-0381"></a>`10.0381` | <i lang="sa-Latn">√māna~</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0382"></a>`10.0382` | <i lang="sa-Latn">√bhū</i> | <i lang="sa-Latn">prāptau</i> |
| <a id="dhatu-10-0383"></a>`10.0383` | <i lang="sa-Latn">√garha~</i> | <i lang="sa-Latn">vinindane</i> |
| <a id="dhatu-10-0384"></a>`10.0384` | <i lang="sa-Latn">√mārga~</i> | <i lang="sa-Latn">anveṣaṇe</i> |
| <a id="dhatu-10-0385"></a>`10.0385` | <i lang="sa-Latn">√kaṭhi~</i> | <i lang="sa-Latn">śoke</i> |
| <a id="dhatu-10-0386"></a>`10.0386` | <i lang="sa-Latn">√mṛjū~</i> | <i lang="sa-Latn">śaucālaṅkārayoḥ</i> |
| <a id="dhatu-10-0387"></a>`10.0387` | <i lang="sa-Latn">√mṛṣa~^</i> | <i lang="sa-Latn">titikṣāyām</i> |
| <a id="dhatu-10-0388"></a>`10.0388` | <i lang="sa-Latn">√dhṛṣa~</i> | <i lang="sa-Latn">prasahane</i> |
| <a id="dhatu-10-0389"></a>`10.0389` | <i lang="sa-Latn">√katha</i> | <i lang="sa-Latn">vākyaprabandhe</i> |
| <a id="dhatu-10-0390"></a>`10.0390` | <i lang="sa-Latn">√vara</i> | <i lang="sa-Latn">īpsāyām</i> |
| <a id="dhatu-10-0391"></a>`10.0391` | <i lang="sa-Latn">√gaṇa</i> | <i lang="sa-Latn">saṅkhyāne</i> |
| <a id="dhatu-10-0392"></a>`10.0392` | <i lang="sa-Latn">√śaṭha</i> | <i lang="sa-Latn">samyagavabhāṣaṇe</i> |
| <a id="dhatu-10-0393"></a>`10.0393` | <i lang="sa-Latn">√śvaṭha</i> | <i lang="sa-Latn">samyagavabhāṣaṇe</i> |
| <a id="dhatu-10-0394"></a>`10.0394` | <i lang="sa-Latn">√paṭha</i> | <i lang="sa-Latn">granthe veṣṭane ca</i> |
| <a id="dhatu-10-0395"></a>`10.0395` | <i lang="sa-Latn">√vaṭha</i> | <i lang="sa-Latn">granthe</i> |
| <a id="dhatu-10-0396"></a>`10.0396` | <i lang="sa-Latn">√raha</i> | <i lang="sa-Latn">tyāge</i> |
| <a id="dhatu-10-0397"></a>`10.0397` | <i lang="sa-Latn">√raṅga~</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0398"></a>`10.0398` | <i lang="sa-Latn">√stana</i> | <i lang="sa-Latn">devaśabde</i> |
| <a id="dhatu-10-0399"></a>`10.0399` | <i lang="sa-Latn">√gada</i> | <i lang="sa-Latn">devaśabde</i> |
| <a id="dhatu-10-0400"></a>`10.0400` | <i lang="sa-Latn">√pata</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0401"></a>`10.0401` | <i lang="sa-Latn">√paṣa</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0402"></a>`10.0402` | <i lang="sa-Latn">√svara</i> | <i lang="sa-Latn">ākṣepe</i> |
| <a id="dhatu-10-0403"></a>`10.0403` | <i lang="sa-Latn">√raca</i> | <i lang="sa-Latn">pratiyatne</i> |
| <a id="dhatu-10-0404"></a>`10.0404` | <i lang="sa-Latn">√kala</i> | <i lang="sa-Latn">gatau saṅkhyāne ca</i> |
| <a id="dhatu-10-0405"></a>`10.0405` | <i lang="sa-Latn">√caha</i> | <i lang="sa-Latn">parikalkane</i> |
| <a id="dhatu-10-0406"></a>`10.0406` | <i lang="sa-Latn">√maha</i> | <i lang="sa-Latn">pūjāyām</i> |
| <a id="dhatu-10-0407"></a>`10.0407` | <i lang="sa-Latn">√sāra</i> | <i lang="sa-Latn">daurbalye</i> |
| <a id="dhatu-10-0408"></a>`10.0408` | <i lang="sa-Latn">√kṛpa</i> | <i lang="sa-Latn">daurbalye</i> |
| <a id="dhatu-10-0409"></a>`10.0409` | <i lang="sa-Latn">√śratha</i> | <i lang="sa-Latn">daurbalye</i> |
| <a id="dhatu-10-0410"></a>`10.0410` | <i lang="sa-Latn">√spṛha</i> | <i lang="sa-Latn">īpsāyām</i> |
| <a id="dhatu-10-0411"></a>`10.0411` | <i lang="sa-Latn">√bhāma</i> | <i lang="sa-Latn">krodhe</i> |
| <a id="dhatu-10-0412"></a>`10.0412` | <i lang="sa-Latn">√sūca</i> | <i lang="sa-Latn">paiśunye</i> |
| <a id="dhatu-10-0413"></a>`10.0413` | <i lang="sa-Latn">√kheṭa</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-10-0414"></a>`10.0414` | <i lang="sa-Latn">√kheḍa~</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-10-0415"></a>`10.0415` | <i lang="sa-Latn">√khoṭa</i> | <i lang="sa-Latn">bhakṣaṇe</i> |
| <a id="dhatu-10-0416"></a>`10.0416` | <i lang="sa-Latn">√kṣoṭa</i> | <i lang="sa-Latn">kṣepe</i> |
| <a id="dhatu-10-0417"></a>`10.0417` | <i lang="sa-Latn">√goma</i> | <i lang="sa-Latn">upalepane</i> |
| <a id="dhatu-10-0418"></a>`10.0418` | <i lang="sa-Latn">√kumāra</i> | <i lang="sa-Latn">krīḍāyām</i> |
| <a id="dhatu-10-0419"></a>`10.0419` | <i lang="sa-Latn">√śīla</i> | <i lang="sa-Latn">upadhāraṇe</i> |
| <a id="dhatu-10-0420"></a>`10.0420` | <i lang="sa-Latn">√sāma</i> | <i lang="sa-Latn">sāntvaprayoge</i> |
| <a id="dhatu-10-0421"></a>`10.0421` | <i lang="sa-Latn">√vela</i> | <i lang="sa-Latn">kālopadeśe</i> |
| <a id="dhatu-10-0422"></a>`10.0422` | <i lang="sa-Latn">√kāla</i> | <i lang="sa-Latn">kālopadeśe</i> |
| <a id="dhatu-10-0423"></a>`10.0423` | <i lang="sa-Latn">√palpūla</i> | <i lang="sa-Latn">lavanavapanayoḥ</i> |
| <a id="dhatu-10-0424"></a>`10.0424` | <i lang="sa-Latn">√vāta</i> | <i lang="sa-Latn">sukhasevanayoḥ</i> |
| <a id="dhatu-10-0425"></a>`10.0425` | <i lang="sa-Latn">√gaveṣa</i> | <i lang="sa-Latn">mārgaṇe</i> |
| <a id="dhatu-10-0426"></a>`10.0426` | <i lang="sa-Latn">√vāsa</i> | <i lang="sa-Latn">upasevāyām</i> |
| <a id="dhatu-10-0427"></a>`10.0427` | <i lang="sa-Latn">√nivāsa</i> | <i lang="sa-Latn">ācchādane</i> |
| <a id="dhatu-10-0428"></a>`10.0428` | <i lang="sa-Latn">√bhāja</i> | <i lang="sa-Latn">pṛthakkarmaṇi</i> |
| <a id="dhatu-10-0429"></a>`10.0429` | <i lang="sa-Latn">√sabhāja</i> | <i lang="sa-Latn">prītidarśanayoḥ prītisevanayoḥ ca</i> |
| <a id="dhatu-10-0430"></a>`10.0430` | <i lang="sa-Latn">√ūna</i> | <i lang="sa-Latn">parihāṇe</i> |
| <a id="dhatu-10-0431"></a>`10.0431` | <i lang="sa-Latn">√dhvana</i> | <i lang="sa-Latn">śabde</i> |
| <a id="dhatu-10-0432"></a>`10.0432` | <i lang="sa-Latn">√kūṭa</i> | <i lang="sa-Latn">paritāpe paridāhe ca</i> |
| <a id="dhatu-10-0433"></a>`10.0433` | <i lang="sa-Latn">√sanketa</i> | <i lang="sa-Latn">āmantraṇe</i> |
| <a id="dhatu-10-0434"></a>`10.0434` | <i lang="sa-Latn">√grāma</i> | <i lang="sa-Latn">āmantraṇe</i> |
| <a id="dhatu-10-0435"></a>`10.0435` | <i lang="sa-Latn">√kuṇa</i> | <i lang="sa-Latn">āmantraṇe</i> |
| <a id="dhatu-10-0436"></a>`10.0436` | <i lang="sa-Latn">√guṇa</i> | <i lang="sa-Latn">āmantraṇe</i> |
| <a id="dhatu-10-0437"></a>`10.0437` | <i lang="sa-Latn">√keta</i> | <i lang="sa-Latn">śrāvaṇe āmantraṇe ca</i> |
| <a id="dhatu-10-0438"></a>`10.0438` | <i lang="sa-Latn">√kūṇa~</i> | <i lang="sa-Latn">saṅkocane</i> |
| <a id="dhatu-10-0439"></a>`10.0439` | <i lang="sa-Latn">√stena</i> | <i lang="sa-Latn">caurye</i> |
| <a id="dhatu-10-0440"></a>`10.0440` | <i lang="sa-Latn">√pada</i> | <i lang="sa-Latn">gatau</i> |
| <a id="dhatu-10-0441"></a>`10.0441` | <i lang="sa-Latn">√gṛha</i> | <i lang="sa-Latn">grahaṇe</i> |
| <a id="dhatu-10-0442"></a>`10.0442` | <i lang="sa-Latn">√mṛga</i> | <i lang="sa-Latn">anveṣaṇe</i> |
| <a id="dhatu-10-0443"></a>`10.0443` | <i lang="sa-Latn">√kuha</i> | <i lang="sa-Latn">vismāpane</i> |
| <a id="dhatu-10-0444"></a>`10.0444` | <i lang="sa-Latn">√śūra</i> | <i lang="sa-Latn">vikrāntau</i> |
| <a id="dhatu-10-0445"></a>`10.0445` | <i lang="sa-Latn">√vīra</i> | <i lang="sa-Latn">vikrāntau</i> |
| <a id="dhatu-10-0446"></a>`10.0446` | <i lang="sa-Latn">√sthūla</i> | <i lang="sa-Latn">paribṛhaṇe</i> |
| <a id="dhatu-10-0447"></a>`10.0447` | <i lang="sa-Latn">√artha</i> | <i lang="sa-Latn">upayācñāyām</i> |
| <a id="dhatu-10-0448"></a>`10.0448` | <i lang="sa-Latn">√satra</i> | <i lang="sa-Latn">santānakriyāyām</i> |
| <a id="dhatu-10-0449"></a>`10.0449` | <i lang="sa-Latn">√garva</i> | <i lang="sa-Latn">māne</i> |
| <a id="dhatu-10-0450"></a>`10.0450` | <i lang="sa-Latn">√sūtra</i> | <i lang="sa-Latn">veṣṭane vimocane granthane ca</i> |
| <a id="dhatu-10-0451"></a>`10.0451` | <i lang="sa-Latn">√mūtra</i> | <i lang="sa-Latn">prasravaṇe</i> |
| <a id="dhatu-10-0452"></a>`10.0452` | <i lang="sa-Latn">√rūkṣa</i> | <i lang="sa-Latn">pāruṣye</i> |
| <a id="dhatu-10-0453"></a>`10.0453` | <i lang="sa-Latn">√pāra</i> | <i lang="sa-Latn">karmasamāptau</i> |
| <a id="dhatu-10-0454"></a>`10.0454` | <i lang="sa-Latn">√tīra</i> | <i lang="sa-Latn">karmasamāptau</i> |
| <a id="dhatu-10-0455"></a>`10.0455` | <i lang="sa-Latn">√puṭa</i> | <i lang="sa-Latn">saṃsarge</i> |
| <a id="dhatu-10-0456"></a>`10.0456` | <i lang="sa-Latn">√katra</i> | <i lang="sa-Latn">śaithilye</i> |
| <a id="dhatu-10-0457"></a>`10.0457` | <i lang="sa-Latn">√karta~</i> | <i lang="sa-Latn">śaithilye</i> |
| <a id="dhatu-10-0458"></a>`10.0458` | <i lang="sa-Latn">√valka</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-10-0459"></a>`10.0459` | <i lang="sa-Latn">√citra</i> | <i lang="sa-Latn">citrīkaraṇe</i> |
| <a id="dhatu-10-0460"></a>`10.0460` | <i lang="sa-Latn">√ansa</i> | <i lang="sa-Latn">samāghāte</i> |
| <a id="dhatu-10-0461"></a>`10.0461` | <i lang="sa-Latn">√vaṭa</i> | <i lang="sa-Latn">vibhājane</i> |
| <a id="dhatu-10-0462"></a>`10.0462` | <i lang="sa-Latn">√chuṭa~</i> | <i lang="sa-Latn">chedane</i> |
| <a id="dhatu-10-0463"></a>`10.0463` | <i lang="sa-Latn">√laja</i> | <i lang="sa-Latn">prakāśane</i> |
| <a id="dhatu-10-0464"></a>`10.0464` | <i lang="sa-Latn">√vaṭi~</i> | <i lang="sa-Latn">prakāśane</i> |
| <a id="dhatu-10-0465"></a>`10.0465` | <i lang="sa-Latn">√laji~</i> | <i lang="sa-Latn">prakāśane</i> |
| <a id="dhatu-10-0466"></a>`10.0466` | <i lang="sa-Latn">√miśra</i> | <i lang="sa-Latn">samparke</i> |
| <a id="dhatu-10-0467"></a>`10.0467` | <i lang="sa-Latn">√sangrāma</i> | <i lang="sa-Latn">yuddhe</i> |
| <a id="dhatu-10-0468"></a>`10.0468` | <i lang="sa-Latn">√stoma</i> | <i lang="sa-Latn">ślāghāyām</i> |
| <a id="dhatu-10-0469"></a>`10.0469` | <i lang="sa-Latn">√chidra</i> | <i lang="sa-Latn">karṇabhedane</i> |
| <a id="dhatu-10-0470"></a>`10.0470` | <i lang="sa-Latn">√karṇa~</i> | <i lang="sa-Latn">bhedane</i> |
| <a id="dhatu-10-0471"></a>`10.0471` | <i lang="sa-Latn">√andha</i> | <i lang="sa-Latn">dṛṣṭyupaghāte</i> |
| <a id="dhatu-10-0472"></a>`10.0472` | <i lang="sa-Latn">√danḍa</i> | <i lang="sa-Latn">daṇḍanipāte</i> |
| <a id="dhatu-10-0473"></a>`10.0473` | <i lang="sa-Latn">√anka</i> | <i lang="sa-Latn">pade lakṣaṇe ca</i> |
| <a id="dhatu-10-0474"></a>`10.0474` | <i lang="sa-Latn">√anga</i> | <i lang="sa-Latn">pade lakṣaṇe ca</i> |
| <a id="dhatu-10-0475"></a>`10.0475` | <i lang="sa-Latn">√sukha</i> | <i lang="sa-Latn">tatkriyāyām</i> |
| <a id="dhatu-10-0476"></a>`10.0476` | <i lang="sa-Latn">√duḥkha</i> | <i lang="sa-Latn">tatkriyāyām</i> |
| <a id="dhatu-10-0477"></a>`10.0477` | <i lang="sa-Latn">√rasa</i> | <i lang="sa-Latn">āsvādanasnehanayoḥ</i> |
| <a id="dhatu-10-0478"></a>`10.0478` | <i lang="sa-Latn">√vyaya</i> | <i lang="sa-Latn">vittasamutsarge</i> |
| <a id="dhatu-10-0479"></a>`10.0479` | <i lang="sa-Latn">√rūpa</i> | <i lang="sa-Latn">rūpakriyāyām</i> |
| <a id="dhatu-10-0480"></a>`10.0480` | <i lang="sa-Latn">√cheda</i> | <i lang="sa-Latn">dvaidhīkaraṇe</i> |
| <a id="dhatu-10-0481"></a>`10.0481` | <i lang="sa-Latn">√chada</i> | <i lang="sa-Latn">apavāraṇe</i> |
| <a id="dhatu-10-0482"></a>`10.0482` | <i lang="sa-Latn">√lābha</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-10-0483"></a>`10.0483` | <i lang="sa-Latn">√vraṇa</i> | <i lang="sa-Latn">gātravicūrṇane</i> |
| <a id="dhatu-10-0484"></a>`10.0484` | <i lang="sa-Latn">√varṇa</i> | <i lang="sa-Latn">varṇakriyāvistāraguṇavacaneṣu</i> |
| <a id="dhatu-10-0485"></a>`10.0485` | <i lang="sa-Latn">√parṇa</i> | <i lang="sa-Latn">haritabhāve</i> |
| <a id="dhatu-10-0486"></a>`10.0486` | <i lang="sa-Latn">√viṣka</i> | <i lang="sa-Latn">darśane</i> |
| <a id="dhatu-10-0487"></a>`10.0487` | <i lang="sa-Latn">√kṣipa</i> | <i lang="sa-Latn">preraṇe</i> |
| <a id="dhatu-10-0488"></a>`10.0488` | <i lang="sa-Latn">√vasa</i> | <i lang="sa-Latn">nivāse</i> |
| <a id="dhatu-10-0489"></a>`10.0489` | <i lang="sa-Latn">√tuttha</i> | <i lang="sa-Latn">āvaraṇe</i> |
| <a id="dhatu-10-0490"></a>`10.0490` | <i lang="sa-Latn">√palyūla</i> | <i lang="sa-Latn">lavanavapanayoḥ</i> |
| <a id="dhatu-10-0491"></a>`10.0491` | <i lang="sa-Latn">√ruṭha~</i> | <i lang="sa-Latn">bhāṣāyām</i> |
| <a id="dhatu-10-0492"></a>`10.0492` | <i lang="sa-Latn">√dheka</i> | <i lang="sa-Latn">darśane</i> |

<a id="gana-11"></a>
## Gaṇa 11 — <i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i> · <span lang="sa-Deva">कण्ड्वादिगणः</span>

[Derivation chapter 11](#chapter-11) · [↑ Contents](#toc)

> Vidyut has no `11.*` rows; this is an explicitly separate supplementary denominative registry.

| Source ID | Dhātu | Meaning/domain |
|---|---|---|
| <a id="dhatu-11-s001"></a>`11.S001` | <i lang="sa-Latn">√kaṇḍūy</i> | supplementary denominative entry; traditional source audit pending |

<a id="preamble-2"></a>
# Preamble 2 — <i lang="sa-Latn">sūtrāṇi</i>: ordered rule registry

Rules are stored once, in Aṣṭādhyāyī order. A chapter derivation links first to its local **Sūtras used in this section** occurrence; that occurrence links here.

<a id="rule-as-1-1-26"></a>
## 1.1.26 — <i lang="sa-Latn">ktaktavatū niṣṭhā</i>

- **Devanāgarī:** <span lang="sa-Deva">क्तक्तवतू निष्ठा</span>
- **Operational record:** The affixes क्त and क्तवतु receive the technical designation निष्ठा.
- **Scope:** `saṃjñā`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 1.1.26](https://ashtadhyayi.com/sutraani/1/1/26)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-3-2-102"></a>
## 3.2.102 — <i lang="sa-Latn">niṣṭhā</i>

- **Devanāgarī:** <span lang="sa-Deva">निष्ठा</span>
- **Operational record:** Introduces the niṣṭhā affixes in the completed-action domain carried into this section.
- **Scope:** `affix-selection`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 3.2.102](https://ashtadhyayi.com/sutraani/3/2/102)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-3-4-70"></a>
## 3.4.70 — <i lang="sa-Latn">tayoreva kṛtyaktakhalarthāḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">तयोरेव कृत्यक्तखलर्थाः</span>
- **Operational record:** Registers the semantic/syntactic domain inherited by kṛtya, kta, and khal-artha formations.
- **Scope:** `semantic-domain`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 3.4.70](https://ashtadhyayi.com/sutraani/3/4/70)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-3-4-72"></a>
## 3.4.72 — <i lang="sa-Latn">gatyarthākarmakaśliṣaśīṅsthāsavasajanaruhajīryatibhyaśca</i>

- **Devanāgarī:** <span lang="sa-Deva">गत्यर्थाकर्मकश्लिषशीङ्स्थासवसजनरुहजीर्यतिभ्यश्च</span>
- **Operational record:** Allows kartari interpretation of क्त after motion roots, intransitives, and the specifically listed roots.
- **Scope:** `voice`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 3.4.72](https://ashtadhyayi.com/sutraani/3/4/72)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-7-2-35"></a>
## 7.2.35 — <i lang="sa-Latn">ārdhadhātukasyeḍ valādeḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">आर्धधातुकस्येड् वलादेः</span>
- **Operational record:** Supplies iṭ before a val-initial ārdhadhātuka affix, subject to the following prohibitions and options.
- **Scope:** `iṭ`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 7.2.35](https://ashtadhyayi.com/sutraani/7/2/35)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-42"></a>
## 8.2.42 — <i lang="sa-Latn">radābhyāṃ niṣṭhāto naḥ pūrvasya ca daḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">रदाभ्यां निष्ठातो नः पूर्वस्य च दः</span>
- **Operational record:** After roots ending in r or d, niṣṭhā t may become n, with the prescribed change of the preceding d.
- **Scope:** `niṣṭhā-phonology`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.42](https://ashtadhyayi.com/sutraani/8/2/42)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-43"></a>
## 8.2.43 — <i lang="sa-Latn">saṃyogāderāto dhātoryaṇvataḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">संयोगादेरातो धातोर्यण्वतः</span>
- **Operational record:** Niṣṭhā substitution in the stated consonant-cluster/ā-root environment.
- **Scope:** `niṣṭhā-phonology`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.43](https://ashtadhyayi.com/sutraani/8/2/43)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-44"></a>
## 8.2.44 — <i lang="sa-Latn">lvādibhyaḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">ल्वादिभ्यः</span>
- **Operational record:** Extends the niṣṭhā substitution to the lexical lū-ādi class.
- **Scope:** `niṣṭhā-phonology`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.44](https://ashtadhyayi.com/sutraani/8/2/44)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-45"></a>
## 8.2.45 — <i lang="sa-Latn">oditaśca</i>

- **Devanāgarī:** <span lang="sa-Deva">ओदितश्च</span>
- **Operational record:** Extends the relevant niṣṭhā operation to roots marked with indicatory o.
- **Scope:** `niṣṭhā-phonology`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.45](https://ashtadhyayi.com/sutraani/8/2/45)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-46"></a>
## 8.2.46 — <i lang="sa-Latn">kṣiyo dīrghāt</i>

- **Devanāgarī:** <span lang="sa-Deva">क्षियो दीर्घात्</span>
- **Operational record:** Special niṣṭhā treatment for kṣi after a long vowel.
- **Scope:** `niṣṭhā-phonology`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.46](https://ashtadhyayi.com/sutraani/8/2/46)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-49"></a>
## 8.2.49 — <i lang="sa-Latn">divo'vijigīṣāyām</i>

- **Devanāgarī:** <span lang="sa-Deva">दिवोऽविजिगीषायाम्</span>
- **Operational record:** Special niṣṭhā result for div outside the stated desiderative sense.
- **Scope:** `lexical-exception`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.49](https://ashtadhyayi.com/sutraani/8/2/49)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-51"></a>
## 8.2.51 — <i lang="sa-Latn">śuṣaḥ kaḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">शुषः कः</span>
- **Operational record:** Prescribes k in the niṣṭhā formation of śuṣ.
- **Scope:** `lexical-exception`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.51](https://ashtadhyayi.com/sutraani/8/2/51)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-52"></a>
## 8.2.52 — <i lang="sa-Latn">paco vaḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">पचो वः</span>
- **Operational record:** Prescribes v in the relevant niṣṭhā formation of pac.
- **Scope:** `lexical-exception`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.52](https://ashtadhyayi.com/sutraani/8/2/52)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-53"></a>
## 8.2.53 — <i lang="sa-Latn">kṣāyo maḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">क्षायो मः</span>
- **Operational record:** Prescribes m for the stated kṣā environment.
- **Scope:** `lexical-exception`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.53](https://ashtadhyayi.com/sutraani/8/2/53)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-55"></a>
## 8.2.55 — <i lang="sa-Latn">anupasargātphullakṣībakṛśollāghāḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">अनुपसर्गात्फुल्लक्षीबकृशोल्लाघाः</span>
- **Operational record:** Lists lexicalized forms in the absence of a preverb.
- **Scope:** `nipātana`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.55](https://ashtadhyayi.com/sutraani/8/2/55)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-56"></a>
## 8.2.56 — <i lang="sa-Latn">nudavidondatrāghrāhrībhyo'nyatarasyām</i>

- **Devanāgarī:** <span lang="sa-Deva">नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्</span>
- **Operational record:** Provides optional niṣṭhā treatment for the listed roots.
- **Scope:** `option`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.56](https://ashtadhyayi.com/sutraani/8/2/56)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-57"></a>
## 8.2.57 — <i lang="sa-Latn">na dhyākhyāpṝmūrchimadām</i>

- **Devanāgarī:** <span lang="sa-Deva">न ध्याख्यापॄमूर्छिमदाम्</span>
- **Operational record:** Blocks the inherited operation for the listed roots.
- **Scope:** `prohibition`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.2.57](https://ashtadhyayi.com/sutraani/8/2/57)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-58"></a>
## 8.2.58 — <i lang="sa-Latn">vitto bhogapratyayayoḥ</i>

- **Devanāgarī:** <span lang="sa-Deva">वित्तो भोगप्रत्यययोः</span>
- **Operational record:** Restricts vitta to the stated meanings.
- **Scope:** `meaning-conditioned`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.58](https://ashtadhyayi.com/sutraani/8/2/58)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-59"></a>
## 8.2.59 — <i lang="sa-Latn">bhittaṃ śakalam</i>

- **Devanāgarī:** <span lang="sa-Deva">भित्तं शकलम्</span>
- **Operational record:** Lexicalizes bhitta in the meaning fragment.
- **Scope:** `meaning-conditioned`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.59](https://ashtadhyayi.com/sutraani/8/2/59)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-2-60"></a>
## 8.2.60 — <i lang="sa-Latn">ṛṇamādhamarṇye</i>

- **Devanāgarī:** <span lang="sa-Deva">ऋणमाधमर्ण्ये</span>
- **Operational record:** Lexical/semantic prescription in the domain of indebtedness.
- **Scope:** `meaning-conditioned`
- **Audit status:** `expand`
- **Source page:** [Aṣṭādhyāyī 8.2.60](https://ashtadhyayi.com/sutraani/8/2/60)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="rule-as-8-4-55"></a>
## 8.4.55 — <i lang="sa-Latn">khari ca</i>

- **Devanāgarī:** <span lang="sa-Deva">खरि च</span>
- **Operational record:** Applies the relevant final devoicing before a khar sound and at pause under inherited conditions.
- **Scope:** `sandhi`
- **Audit status:** `core`
- **Source page:** [Aṣṭādhyāyī 8.4.55](https://ashtadhyayi.com/sutraani/8/4/55)

[↑ Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-01"></a>
# Chapter 1 — <i lang="sa-Latn">bhvādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">भ्वादिगणः</span>

[Gaṇa 1 in Preamble 1](#gana-01) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-01-rules"></a>
## Sūtras used in this section

<a id="use-g01-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g01-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.
<a id="use-g01-as-3-4-72-u01"></a>
- **AS-3-4-72 local use:** [<i lang="sa-Latn">gatyarthākarmakaśliṣaśīṅsthāsavasajanaruhajīryatibhyaśca</i>](#rule-as-3-4-72) — Allows kartari interpretation of क्त after motion roots, intransitives, and the specifically listed roots.
<a id="use-g01-as-8-2-52-u01"></a>
- **AS-8-2-52 local use:** [<i lang="sa-Latn">paco vaḥ</i>](#rule-as-8-2-52) — Prescribes v in the relevant niṣṭhā formation of pac.

## Derivation bars

<a id="deriv-g01-bu-kta"></a>
### <i lang="sa-Latn">√bhū</i> → <i lang="sa-Latn">bhūta</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√bhū</i>](#dhatu-01-0001); Dhātupāṭha `01.0001`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g01-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g01-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-3-4-72`. | [local AS-3-4-72](#use-g01-as-3-4-72-u01) |
| Audit result | <i lang="sa-Latn">bhūta</i>. Initial model; full internal vowel derivation is an expansion point. | [CAT-REGULAR-TA](#category-cat-regular-ta), [CAT-KARTARI](#category-cat-kartari) |

<a id="deriv-g01-gam-kta"></a>
### <i lang="sa-Latn">√gam</i> → <i lang="sa-Latn">gata</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√gam</i>](#dhatu-01-1004); Dhātupāṭha `01.1004`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g01-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g01-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-3-4-72`. | [local AS-3-4-72](#use-g01-as-3-4-72-u01) |
| Audit result | <i lang="sa-Latn">gata</i>. Motion-root kartari interpretation. | [CAT-REGULAR-TA](#category-cat-regular-ta), [CAT-KARTARI](#category-cat-kartari) |

<a id="deriv-g01-pac-kta"></a>
### <i lang="sa-Latn">√pac</i> → <i lang="sa-Latn">pakva</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√pac</i>](#dhatu-01-0198); Dhātupāṭha `01.0198`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g01-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g01-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-8-2-52`. | [local AS-8-2-52](#use-g01-as-8-2-52-u01) |
| Audit result | <i lang="sa-Latn">pakva</i>. Lexically governed niṣṭhā outcome. | [CAT-LEXICAL](#category-cat-lexical), [CAT-KARMANI](#category-cat-karmani) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

- [<i lang="sa-Latn">√pac</i> → <i lang="sa-Latn">pakva</i>](#deriv-g01-pac-kta)

[↑ Chapter beginning](#chapter-01) · [↑ Contents](#toc)

<a id="chapter-02"></a>
# Chapter 2 — <i lang="sa-Latn">adādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">अदादिगणः</span>

[Gaṇa 2 in Preamble 1](#gana-02) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-02-rules"></a>
## Sūtras used in this section

<a id="use-g02-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g02-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.
<a id="use-g02-as-8-2-56-u01"></a>
- **AS-8-2-56 local use:** [<i lang="sa-Latn">nudavidondatrāghrāhrībhyo'nyatarasyām</i>](#rule-as-8-2-56) — Provides optional niṣṭhā treatment for the listed roots.
<a id="use-g02-as-8-2-58-u01"></a>
- **AS-8-2-58 local use:** [<i lang="sa-Latn">vitto bhogapratyayayoḥ</i>](#rule-as-8-2-58) — Restricts vitta to the stated meanings.

## Derivation bars

<a id="deriv-g02-vid-kta"></a>
### <i lang="sa-Latn">√vid</i> → <i lang="sa-Latn">vitta / vidita</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√vid</i>](#dhatu-02-0059); Dhātupāṭha `02.0059`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g02-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g02-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-8-2-56`. | [local AS-8-2-56](#use-g02-as-8-2-56-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-8-2-58`. | [local AS-8-2-58](#use-g02-as-8-2-58-u01) |
| Audit result | <i lang="sa-Latn">vitta / vidita</i>. Meaning and optionality must be separated. | [CAT-OPTIONAL](#category-cat-optional), [CAT-LEXICAL](#category-cat-lexical) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

- [<i lang="sa-Latn">√vid</i> → <i lang="sa-Latn">vitta / vidita</i>](#deriv-g02-vid-kta)

[↑ Chapter beginning](#chapter-02) · [↑ Contents](#toc)

<a id="chapter-03"></a>
# Chapter 3 — <i lang="sa-Latn">juhotyādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">जुहोत्यादिगणः</span>

[Gaṇa 3 in Preamble 1](#gana-03) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-03-rules"></a>
## Sūtras used in this section

<a id="use-g03-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g03-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">juhotyādi-gaṇaḥ</i>](#gana-03). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g03-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g03-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-03) · [↑ Contents](#toc)

<a id="chapter-04"></a>
# Chapter 4 — <i lang="sa-Latn">divādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">दिवादिगणः</span>

[Gaṇa 4 in Preamble 1](#gana-04) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-04-rules"></a>
## Sūtras used in this section

<a id="use-g04-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g04-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.
<a id="use-g04-as-8-2-51-u01"></a>
- **AS-8-2-51 local use:** [<i lang="sa-Latn">śuṣaḥ kaḥ</i>](#rule-as-8-2-51) — Prescribes k in the niṣṭhā formation of śuṣ.

## Derivation bars

<a id="deriv-g04-suz-kta"></a>
### <i lang="sa-Latn">√śuṣ</i> → <i lang="sa-Latn">śuṣka</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√śuṣ</i>](#dhatu-04-0080); Dhātupāṭha `04.0080`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g04-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g04-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-8-2-51`. | [local AS-8-2-51](#use-g04-as-8-2-51-u01) |
| Audit result | <i lang="sa-Latn">śuṣka</i>. Special k-substitution. | [CAT-LEXICAL](#category-cat-lexical) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

- [<i lang="sa-Latn">√śuṣ</i> → <i lang="sa-Latn">śuṣka</i>](#deriv-g04-suz-kta)

[↑ Chapter beginning](#chapter-04) · [↑ Contents](#toc)

<a id="chapter-05"></a>
# Chapter 5 — <i lang="sa-Latn">svādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">स्वादिगणः</span>

[Gaṇa 5 in Preamble 1](#gana-05) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-05-rules"></a>
## Sūtras used in this section

<a id="use-g05-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g05-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">svādi-gaṇaḥ</i>](#gana-05). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g05-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g05-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-05) · [↑ Contents](#toc)

<a id="chapter-06"></a>
# Chapter 6 — <i lang="sa-Latn">tudādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">तुदादिगणः</span>

[Gaṇa 6 in Preamble 1](#gana-06) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-06-rules"></a>
## Sūtras used in this section

<a id="use-g06-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g06-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">tudādi-gaṇaḥ</i>](#gana-06). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g06-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g06-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-06) · [↑ Contents](#toc)

<a id="chapter-07"></a>
# Chapter 7 — <i lang="sa-Latn">rudhādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">रुधादिगणः</span>

[Gaṇa 7 in Preamble 1](#gana-07) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-07-rules"></a>
## Sūtras used in this section

<a id="use-g07-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g07-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">rudhādi-gaṇaḥ</i>](#gana-07). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g07-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g07-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-07) · [↑ Contents](#toc)

<a id="chapter-08"></a>
# Chapter 8 — <i lang="sa-Latn">tanādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">तनादिगणः</span>

[Gaṇa 8 in Preamble 1](#gana-08) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-08-rules"></a>
## Sūtras used in this section

<a id="use-g08-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g08-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

<a id="deriv-g08-kf-kta"></a>
### <i lang="sa-Latn">√kṛ</i> → <i lang="sa-Latn">kṛta</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√kṛ</i>](#gana-08); gaṇa registry; exact source row awaits audit. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g08-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g08-as-1-1-26-u01) |
| Audit result | <i lang="sa-Latn">kṛta</i>. Canonical high-frequency model. | [CAT-REGULAR-TA](#category-cat-regular-ta), [CAT-KARMANI](#category-cat-karmani) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-08) · [↑ Contents](#toc)

<a id="chapter-09"></a>
# Chapter 9 — <i lang="sa-Latn">kryādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">क्र्यादिगणः</span>

[Gaṇa 9 in Preamble 1](#gana-09) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-09-rules"></a>
## Sūtras used in this section

<a id="use-g09-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g09-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">kryādi-gaṇaḥ</i>](#gana-09). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g09-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g09-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-09) · [↑ Contents](#toc)

<a id="chapter-10"></a>
# Chapter 10 — <i lang="sa-Latn">curādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">चुरादिगणः</span>

[Gaṇa 10 in Preamble 1](#gana-10) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-10-rules"></a>
## Sūtras used in this section

<a id="use-g10-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g10-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.

## Derivation bars

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | Select an exact entry from [<i lang="sa-Latn">curādi-gaṇaḥ</i>](#gana-10). | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g10-as-3-2-102-u01) |
| Technical designation | Register it as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g10-as-1-1-26-u01) |
| Expansion point | Add a root-specific bar only together with every newly invoked local rule use. | [Preamble 2](#preamble-2) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-10) · [↑ Contents](#toc)

<a id="chapter-11"></a>
# Chapter 11 — <i lang="sa-Latn">kaṇḍvādi-gaṇaḥ-padam</i> · <span lang="sa-Deva">कण्ड्वादिगणः</span>

[Gaṇa 11 in Preamble 1](#gana-11) · [Preamble 2](#preamble-2) · [↑ Contents](#toc)

<a id="chapter-11-rules"></a>
## Sūtras used in this section

<a id="use-g11-as-1-1-26-u01"></a>
- **AS-1-1-26 local use:** [<i lang="sa-Latn">ktaktavatū niṣṭhā</i>](#rule-as-1-1-26) — The affixes क्त and क्तवतु receive the technical designation निष्ठा.
<a id="use-g11-as-3-2-102-u01"></a>
- **AS-3-2-102 local use:** [<i lang="sa-Latn">niṣṭhā</i>](#rule-as-3-2-102) — Introduces the niṣṭhā affixes in the completed-action domain carried into this section.
<a id="use-g11-as-7-2-35-u01"></a>
- **AS-7-2-35 local use:** [<i lang="sa-Latn">ārdhadhātukasyeḍ valādeḥ</i>](#rule-as-7-2-35) — Supplies iṭ before a val-initial ārdhadhātuka affix, subject to the following prohibitions and options.

## Derivation bars

<a id="deriv-g11-karquy-kta"></a>
### <i lang="sa-Latn">√kaṇḍūy</i> → <i lang="sa-Latn">kaṇḍūyita</i>

| Bar | Recorded operation | Linked authority |
|---|---|---|
| Root identity | [<i lang="sa-Latn">√kaṇḍūy</i>](#dhatu-11-s001); supplementary entry `11.S001`. | [Preamble 1](#preamble-1) |
| Affix selection | Introduce <i lang="sa-Latn">⟨kta⟩</i>. | [local AS-3-2-102](#use-g11-as-3-2-102-u01) |
| Technical designation | Register <i lang="sa-Latn">⟨kta⟩</i> as <i lang="sa-Latn">niṣṭhā</i>. | [local AS-1-1-26](#use-g11-as-1-1-26-u01) |
| Rule-conditioned operation | Apply only in the environment recorded for `AS-7-2-35`. | [local AS-7-2-35](#use-g11-as-7-2-35-u01) |
| Audit result | <i lang="sa-Latn">kaṇḍūyita</i>. Denominative/kandvādi expansion model. | [CAT-IT-TA](#category-cat-it-ta) |

## Sandhi rules employed in this chapter

— No sandhi rule is invoked by the currently audited derivation bars.

## Irregular constructions in this gaṇa

—

[↑ Chapter beginning](#chapter-11) · [↑ Contents](#toc)

<a id="sandhi-registry"></a>
# Sandhi rules employed

| Rule | Sanskrit | Actual chapter uses |
|---|---|---|
| [AS-8-4-55](#rule-as-8-4-55) | <i lang="sa-Latn">khari ca</i> | registered; not yet invoked |

[↑ Contents](#toc)

<a id="composition-categories"></a>
# Categories of composition

<a id="category-cat-regular-ta"></a>
## <i lang="sa-Latn">pratyakṣatakārāntaḥ</i> · <span lang="sa-Deva">प्रत्यक्षतकारान्तः</span>

Surface -ta remains directly visible.

- [<i lang="sa-Latn">√bhū</i> → <i lang="sa-Latn">bhūta</i>](#deriv-g01-bu-kta)
- [<i lang="sa-Latn">√gam</i> → <i lang="sa-Latn">gata</i>](#deriv-g01-gam-kta)
- [<i lang="sa-Latn">√kṛ</i> → <i lang="sa-Latn">kṛta</i>](#deriv-g08-kf-kta)

<a id="category-cat-it-ta"></a>
## <i lang="sa-Latn">iḍāgamayuktaḥ</i> · <span lang="sa-Deva">इडागमयुक्तः</span>

iṭ appears before क्त under the ārdhadhātuka iṭ system.

- [<i lang="sa-Latn">√kaṇḍūy</i> → <i lang="sa-Latn">kaṇḍūyita</i>](#deriv-g11-karquy-kta)

<a id="category-cat-natva-nistha"></a>
## <i lang="sa-Latn">niṣṭhānatvam</i> · <span lang="sa-Deva">निष्ठानत्वम्</span>

The niṣṭhā dental undergoes n-substitution under 8.2.42ff.

—

<a id="category-cat-lexical"></a>
## <i lang="sa-Latn">nipātitaviśeṣaḥ</i> · <span lang="sa-Deva">निपातितविशेषः</span>

The output depends on a lexical or meaning-conditioned prescription.

- [<i lang="sa-Latn">√pac</i> → <i lang="sa-Latn">pakva</i>](#deriv-g01-pac-kta)
- [<i lang="sa-Latn">√vid</i> → <i lang="sa-Latn">vitta / vidita</i>](#deriv-g02-vid-kta)
- [<i lang="sa-Latn">√śuṣ</i> → <i lang="sa-Latn">śuṣka</i>](#deriv-g04-suz-kta)

<a id="category-cat-optional"></a>
## <i lang="sa-Latn">vikalpitaḥ</i> · <span lang="sa-Deva">विकल्पितः</span>

More than one derivation is licensed.

- [<i lang="sa-Latn">√vid</i> → <i lang="sa-Latn">vitta / vidita</i>](#deriv-g02-vid-kta)

<a id="category-cat-kartari"></a>
## <i lang="sa-Latn">kartari ktaḥ</i> · <span lang="sa-Deva">कर्तरि क्तः</span>

The क्त form receives kartari interpretation under 3.4.72.

- [<i lang="sa-Latn">√bhū</i> → <i lang="sa-Latn">bhūta</i>](#deriv-g01-bu-kta)
- [<i lang="sa-Latn">√gam</i> → <i lang="sa-Latn">gata</i>](#deriv-g01-gam-kta)

<a id="category-cat-karmani"></a>
## <i lang="sa-Latn">karmaṇi ktaḥ</i> · <span lang="sa-Deva">कर्मणि क्तः</span>

The ordinary passive/resultative interpretation.

- [<i lang="sa-Latn">√pac</i> → <i lang="sa-Latn">pakva</i>](#deriv-g01-pac-kta)
- [<i lang="sa-Latn">√kṛ</i> → <i lang="sa-Latn">kṛta</i>](#deriv-g08-kf-kta)

[↑ Contents](#toc)

<a id="irregular-by-gana"></a>
# Irregular constructions by gaṇa

## Gaṇa 1 — <i lang="sa-Latn">bhvādi-gaṇaḥ</i>
- [<i lang="sa-Latn">√pac</i> → <i lang="sa-Latn">pakva</i>](#deriv-g01-pac-kta) — Lexically governed niṣṭhā outcome.

## Gaṇa 2 — <i lang="sa-Latn">adādi-gaṇaḥ</i>
- [<i lang="sa-Latn">√vid</i> → <i lang="sa-Latn">vitta / vidita</i>](#deriv-g02-vid-kta) — Meaning and optionality must be separated.

## Gaṇa 3 — <i lang="sa-Latn">juhotyādi-gaṇaḥ</i>
—

## Gaṇa 4 — <i lang="sa-Latn">divādi-gaṇaḥ</i>
- [<i lang="sa-Latn">√śuṣ</i> → <i lang="sa-Latn">śuṣka</i>](#deriv-g04-suz-kta) — Special k-substitution.

## Gaṇa 5 — <i lang="sa-Latn">svādi-gaṇaḥ</i>
—

## Gaṇa 6 — <i lang="sa-Latn">tudādi-gaṇaḥ</i>
—

## Gaṇa 7 — <i lang="sa-Latn">rudhādi-gaṇaḥ</i>
—

## Gaṇa 8 — <i lang="sa-Latn">tanādi-gaṇaḥ</i>
—

## Gaṇa 9 — <i lang="sa-Latn">kryādi-gaṇaḥ</i>
—

## Gaṇa 10 — <i lang="sa-Latn">curādi-gaṇaḥ</i>
—

## Gaṇa 11 — <i lang="sa-Latn">kaṇḍvādi-gaṇaḥ</i>
—

[↑ Contents](#toc)

<a id="sources"></a>
# Sources and generation contract

- Complete Dhātupāṭha registry: [Vidyut `dhatupatha.tsv`](https://raw.githubusercontent.com/ambuda-org/vidyut/main/vidyut-prakriya/data/dhatupatha.tsv).
- Rule texts and operational records: [`data/rules.json`](../../data/rules.json).
- Examples: [`data/examples.json`](../../data/examples.json).
- Composition categories: [`data/categories.json`](../../data/categories.json).
- Generator: [`scripts/generate_markdown_proof.py`](../../scripts/generate_markdown_proof.py).

The generated Markdown is the proof-of-work endpoint. Source registries and tooling remain editable elsewhere in the repository; this folder contains only the human-readable project artifact.

[↑ Contents](#toc)
