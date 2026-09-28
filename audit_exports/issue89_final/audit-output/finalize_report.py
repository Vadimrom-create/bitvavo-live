"""Finalize report with availability-corrected comparisons and gate appendix."""
from replay import *
import csv,statistics

def R(n):return json.loads((OUT/(n+'.json')).read_text())
def table(h,rs):return '\n'.join(['| '+' | '.join(h)+' |','|'+'|'.join(['---']*len(h))+'|']+['| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rs])
def f(x,n=2):return 'ND' if x is None or isinstance(x,str) else f'{x:.{n}f}'
def time(s):return s.replace('2026-09-','').replace('T',' ').replace('+00:00','').replace('Z','')
metrics=R('final_metrics');cohorts=R('final_cohorts');deltas=R('final_deltas');gates=R('seven_gate_details');rv=R('revalidation_summary')
report=(OUT/'Audit_Solaire_2026-09-27.md').read_text()
report=report.replace('## Périmètre, causalité et preuves','''**Version finale :** reprise vérifiée jusqu’au HEAD `44d7e50b9825a439f541fac036d8276bea6837b1` (27/09 21:29:15 UTC) : 97 commits supplémentaires depuis `1ee4d8`, aucun changement Python/workflow. Le workspace d’audit n’est pas un checkout Git ; un ancien checkout distinct reste sur `3235924` avec deux archives déjà modifiées. Il n’a pas été touché. Le correctif chronologique existe dans le replay d’audit, **pas dans le code de production**. Aucun commit/PR de production n’est revendiqué.

**Correction d’horodatage indispensable :** les timestamps `decision_ts` BUY_SENT du journal reprennent `checked_at_utc`, fixé au début du sender. Ils ne datent pas la fin du gate ou la réception utilisateur. Les 125 BUY ont été joints à 111 emails Gmail ; les résultats définitifs de la section D utilisent leur disponibilité Gmail. Deux entrées changent de bougie par rapport au calcul initial. Les timestamps journal sont conservés comme preuves de trace, sans les faire passer pour des heures exactes de disponibilité. Les résultats initiaux sont conservés dans le pack ; ils ne sont pas les résultats économiques finaux.

## Périmètre, causalité et preuves''')
# Correct overprecise labels without losing original evidence timestamps.
report=report.replace('| Décision production |','| Journal BUY_SENT, début du contrôle |').replace('| BUY_SENT |','| Journal BUY_SENT, début du contrôle |').replace('| Premier BUY_SENT |','| Premier BUY_SENT, horodatage de début |').replace('| BUY_SENT suivant |','| BUY_SENT suivant, horodatage de début |')
report=report.replace('QNT et KMNO','QNT et KMNO')
extra='''
## 3 bis. Détail contradictoire des sept actifs et des revalidations

La classification conserve une quatrième possibilité, **indéterminé**, quand les données ne permettent pas de choisir honnêtement entre protecteur et trop conservateur. La hausse future n’intervient jamais dans cette décision. Le fichier `all_seven_gate_events.csv` détaille chaque événement avec timestamp, prix signal, motif et limite de preuve.

| Actif | Rejets de production avant cutoff | Premier instant technique documenté | Appréciation causale du gate |
|---|---|---|---|
| AMP | 5 volume, puis 8 spread ; aucun BUY | 26/09 18:57:37.113672 V3 READY ; V3.1 SELECTABLE à 19:07:29.238372 | Les refus volume antérieurs restent indéterminés faute de carnet contemporain. Les refus spread respectent le plafond, leur coût exact n’est pas journalisé. À 19:09:01 le suivi de rejet retrouve une exécution propre mais le signal est BUILDING 5,081, donc **pas éligible à un BUY production**. Le premier fully actionable de ce suivi est le 27/09 05:41, hors fenêtre. |
| HFT | 9 volume ; aucun BUY | Non établi | Premier rejet 21/09 13:56:20.167155, signal 0,005314. Volume inférieur au seuil ; pas de carnet de gate ni de READY ultérieur prouvé. Impossible de classer « trop conservateur pour 100 € » avec le +28,69 %. |
| 2Z | 2 range, 1 spread, 2 stop ; aucun BUY | 24/09 14:42:21.893310 V3 READY ; V3.1 14:43:35.159205 | Le range V3 de 5,950593 % montre une frontière structurelle proche de 6 %, avec profondeur100 valide. Ce n’est pas la preuve que toute baisse de seuil est bonne. Après rejet spread 16:53:11.999954, contrôle shadow propre à 16:55:09.997647 ; disponible dans un commit à **16:55:25**. Le refus spread ancien devient obsolète pour cette nouvelle quote, mais le trade plus tardif perd dans C3. |
| RUNE | 1 range ; aucun BUY avant cutoff | 26/09 09:21:15.284183 V3 READY technique | Premier rejet 22/09 13:18:59.284728 à 0,57712. Au READY du 26, range encore 3,632332 % : reste sous 6 et 5 %. Exécution mécanique100/150 plausible, mais V3.1 refuse le score économique à 09:28:06.683830 (5,287), puis 11:36:00.419025 (5,59). Aucun achat économique validé ne doit être inventé. |
| COW | 1 volume ; aucun BUY | Non établi | Rejet 24/09 14:42:12.992751 à 0,12603. Aucun READY ni carnet approprié permettant le recalcul. WIDE_SPREAD_RISK du DL est une route parallèle, pas la cause de ce veto sender. |
| RARE | 5 volume, 6 stop, 3 spread, **2 BUY** | V3 READY 25/09 17:47:23.698099 ; production reçue à 21:32:50 à **0,014528 €** | Le READY de 17:47 est rejeté économiquement à 17:53:15.915791, score5,074. 150 € excède le risque12 sur ce plan. Après un autre refus stop le 26 à17:44, revalidation propre à17:53:17.072912, publiée17:53:32, sans nouvelle alerte production. Le prix 0,020686 est le PASS shadow du 26, pas le premier achat. |
| AGI | 8 volume, 1 spread ; aucun BUY | 26/09 22:44:28.956561 READY technique | Le carnet permet de chiffrer l’entrée, mais pas la liquidité future de sortie. À150, impact0,1791 % dépasse le cap conservateur0,10 % du prototype. Pas de V3.1 SELECTABLE ni horizon4h mature ; le +24h n’est pas une preuve de trade capturable. |

**Bornes sur les refus sans mesures conservées.** SPREAD_TOO_WIDE signifie spread>0,5 %, soit coût top-book >0,4975 € pour100 et >0,7463 € pour150, avant frais et impact. STRUCTURAL_STOP_TOO_WIDE signifie distance>10 % : à150, risque brut>15 €, donc ce refus protège effectivement le budget12 € ; à100, la distance exacte est nécessaire pour savoir si un sizing100 suffit. STRUCTURAL_RANGE_TOO_NARROW est une règle structurelle, non une preuve de carnet insuffisant. INSUFFICIENT_EXECUTION_LIQUIDITY indique volume24h<75000 €, sans mesure de VWAP par ce chemin. Aucun de ces journaux n’autorise à inventer le nombre manquant.

### Premières exécutions techniques conservées — 100 / 150 €

Les mesures sont celles de l’instant indiqué, jamais reportées sur les refus antérieurs. « ≥100 » signifie que le benchmark100 est rempli, sans inventer la profondeur totale ni un VWAP150. La qualification économique est indiquée séparément plus haut.
'''
rs=[]
for g in gates:
 if g['first_ready']=='NOT_FOUND':rs.append([g['market'],'Non établi']+['ND']*8);continue
 dep=g.get('ask25_eur');dep=f(dep) if isinstance(dep,(int,float)) else '≥100 ; total ND'
 rs.append([g['market'],time(g['first_ready']),f(g['spread'],4),dep,f"{g['vwap100']:.12g} / "+(f"{g['vwap150']:.12g}" if isinstance(g.get('vwap150'),(int,float)) else 'ND'),f"{g['impact100']:.4f} / "+f(g.get('impact150'),4),f(g['range'],4),f"{g['stop']:.12g} ({g['stop_pct']:.4f} %)",f(g['risk100'])+' / '+f(g['risk150']),f(g.get('cost_spread100'),3)+' / '+f(g.get('cost_spread150'),3)])
extra+=table(['Actif','Disponible UTC','Spread %','Asks €','VWAP100 /150','Impact %100 /150','Range %','Stop € (%distance)','Risque €100 /150','Spread €100 /150'],rs)
extra+='''

### 2Z : le pattern REJECT → conditions améliorées → pas de BUY

- 24/09 14:42:12.992751 : refus production range, signal0,04775. Neuf secondes plus tard, V3 a une entrée0,04809, stop0,045657, range5,950593 %, spread0,127 %, benchmark100 sur un niveau sans impact ; risque100≈5,63 €, risque150 non certifié faute de profondeur brute à cet instant.
- 16:53:11.999954 : nouveau refus production SPREAD_TOO_WIDE, signal0,052384.
- 16:55:09.997647 : début du contrôle shadow enregistré ; résultat validé avec entrée0,051556, stop0,047122, spread0,326925 %, range13,816184 %, distance stop8,600357 %, score8,5, quatre preuves, CONFIRMED_ACCELERATION. **Publication GitHub à16:55:25** : borne vérifiable à laquelle tout le résultat existe.
- À la quote validée, risque estimé100≈9,15 € et150≈13,72 € ; coût top-book≈0,326 /0,489 €. Pas de profondeur brute dans ce snapshot : VWAP/slippage100/150 non certifiés. 150 est exclu par le budget12, 100 reste un candidat au modèle.
- Aucun BUY production 2Z dans la fenêtre. Le suivi de rejet est explicitement shadow ; il ne déclenche pas le sender. C’est un défaut possible de routage/reprise, pas une panne SMTP et pas une preuve que l’ancien rejet spread était erroné.
- C3 à100 simule une entrée17:00 à0,051692641 : MFE4h+1,69 %, MAE−3,96 %, stop non touché, PnL net−4,45 €. La reprise automatique ajoute ici **un trade perdant**, malgré le statut de gagnant quotidien de2Z.

### Généralisation, sans sélection des futurs non-alertés

467 commits du journal de rejet ont été recensés ; 86 versions précises relues contiennent 96 revalidations confirmées sur63 marchés. Les timestamps de publication bornent leur disponibilité, de0,71 à33,87 secondes après le début de contrôle. Les snapshots postérieurs au cutoff, dont le fully actionable AMP du27 à05:41, sont exclus.

Sur94 revalidations avec quatre heures d’observation disponibles,90 n’ont aucun BUY production dans ces quatre heures. **Ce ne sont pas90 faux négatifs économiques.** `fully_actionable` dans ce journal signifie confirmé + exécution valide ; le script n’applique pas le contrôle de thèse antérieure. En le conservant de manière prudente,74 des96 cas sont retenus ;22 seulement deviennent candidats à la reprise. La sélection C3 ne regarde jamais si un BUY apparaîtra ensuite ; cette absence future sert uniquement au diagnostic.

C3 reprend une seule fois chaque événement validé, à sa première publication connue, avec quote âgée de moins de90s, score≥6,5, preuves≥3, et protection des alertes antérieures encore actives. Faute d’identifiant d’épisode suffisant dans ce snapshot, aucun bypass « nouvel épisode » n’est inventé : traitement conservateur. Capital, risque et exécution modélisée sont ensuite identiques aux autres variantes.
'''
report=report.replace('## A. Diagnostic transversal',extra+'\n\n## A. Diagnostic transversal')
newd='''## D. Comparaison économique définitive — causalité et contrôles négatifs

**Ces tableaux remplacent les valeurs du replay initial basé sur l’heure du début du sender.** La correction de disponibilité ne change ni les seuils ni les choix de variantes. 125 BUY sont rapprochés d’emails ; deux franchissent une frontière5min. TREAD du21 est un exemple : début contrôle10:04:59, email10:05:02. Entrer à10:05 sur la seule trace journal aurait devancé l’email ; le test isolé prend désormais la bougie suivante et obtient NO_FILL.

**Fenêtre principale commune aux quatre variantes : 23/09 23:22:23.220478 → 27/09 00:25 UTC pour les prix complets**, décisions limitées au snapshot00:47. Tous les candidats de l’univers disponibles dans cette fenêtre sont éligibles, pas uniquement les dix gagnants. B reprend les BUY réellement envoyés ; C1 ajoute les confirmations range5 préexistantes ; C2 ajoute les qualifications V3.1 ; C3 ajoute les revalidations après protections conservées. Les comparaisons complètes depuis le21 sont aussi conservées pour ne pas effacer le résultat défavorable de C1 dans la fenêtre initiale.

Modèle fixé : capital2331,61 € fictif, max10positions, une par marché, 100 ou150 € frais inclus, risque≤12 €. Entrée au premier open5min après disponibilité ×1,001, limite quote×1,005 ; frais0,25 %/côté. Stop structurel inchangé, gap et sortie−0,10 % ; sinon clôture après4h. Sensibilité24h, sans choisir l’horizon favorable a posteriori. C1 utilise le timestamp enregistré après validation ; C2 la décision qualifiée avec plan déjà disponible ; C3 la publication de son résultat. Les heures et prix futurs ne servent qu’à mesurer l’exécution modélisée et les résultats, jamais à choisir les candidats.

Les bid depths complets, latences humaines et frais réels de compte restent manquants : il s’agit d’un replay causal avec **modèle de fill**, pas d’ordres certifiés. Les bougies sont triées, complètes et évaluées jusqu’au cutoff. Les horizons non matures sont censurés. MFE/MAE sur tout l’horizon incluent potentiellement l’après-stop ; les fichiers donnent aussi les excursions jusqu’à la bougie de sortie, sans prétendre connaître l’ordre intrabar.

### Même fenêtre, horizon4h
'''
common=[m for m in metrics if m['horizon_hours']==4 and not m['policy'].startswith('F_full')]
newd+=table(['Variante','€','Trades','Gagnants/perdants','Réussite %','Espérance €','PnL €','DD MTM €','Stops','Turnover achat €','Cibles capturées'],[[m['policy'],m['stake'],m['fills'],f"{m['wins']}/{m['losses']}",f(m['win_rate_pct']),f(m['expectancy_eur']),f(m['net_pnl_eur']),f(m['mtm_drawdown_eur']),m['stops'],m['buy_turnover_eur'],', '.join(m['targets_captured'])] for m in common])
newd+='\n\n### MFE/MAE et contrôles hors des dix gagnants\n\nLes « contrôles négatifs » désignent ici tous les marchés hors de la liste adversariale, y compris leurs trades gagnants : on ne fabrique pas un groupe de contrôle en ne gardant que les perdants après coup.\n\n'
newd+=table(['Variante','€','Cohorte','Trades','Gagnants/perdants','PnL €','MFE médiane %','MAE médiane %','Stops'],[[c['policy'],c['stake'],c['cohort'],c['trades'],f"{c['wins']}/{c['losses']}",f(c['pnl']),f(c['median_mfe']),f(c['median_mae']),c['stops']] for c in cohorts if c['horizon']==4 and not c['policy'].startswith('F_full')])
newd+='\n\n### Faux positifs ajoutés et trades déplacés\n\nUn faux positif est défini ici comme un trade au PnL net négatif sous la sortie fixée. Une hausse24h ne définit pas le succès d’une entrée.\n\n'
newd+=table(['Variante','€','Trades supplémentaires distincts','Dont perdants','Baseline déplacés','Dont perdants','Cibles supplémentaires'],[[d['policy'],d['stake'],d['extra_trades'],d['extra_losers'],d['displaced'],d['displaced_losers'],', '.join(d['extra_targets'])] for d in deltas if d['horizon']==4 and not d['policy'].startswith('F_full')])
newd+='''

À100 sur cette fenêtre commune, C1 améliore seulement le total de1,55 € mais augmente le drawdown d’environ23,71 € ; son espérance reste négative. C2 réduit la perte totale d’environ19,74 € mais ajoute45 perdants nets et augmente le drawdown. C3 ajoute9 trades distincts, dont5 perdants, et déplace1 baseline : PnL dégradé d’environ13,54 €, drawdown accru. À150, C3 améliore légèrement le total mais reste déficitaire, sur très peu d’ajouts ; ce n’est pas une validation.

### Fenêtre initiale depuis le21 — ne pas réécrire le résultat défavorable de C1
'''
newd+=table(['Variante','€','Trades','Gagnants/perdants','PnL €','DD MTM €'],[[m['policy'],m['stake'],m['fills'],f"{m['wins']}/{m['losses']}",f(m['net_pnl_eur']),f(m['mtm_drawdown_eur'])] for m in metrics if m['policy'].startswith('F_full')])
newd+='''

À100 dans la fenêtre initiale, C1 reste moins bon de14,61 € malgré2Z capturé. Le changement de deux bougies dû aux emails déplace le niveau des résultats, pas cette comparaison. C3 dégrade aussi le résultat à100. Aucun choix de sous-fenêtre ne doit transformer ces variantes en stratégie promouvable.

### Sensibilité24h sur la même fenêtre principale
'''
newd+=table(['Variante','€','Trades','Gagnants/perdants','PnL €','Espérance €','DD MTM €','Stops','Censurés'],[[m['policy'],m['stake'],m['fills'],f"{m['wins']}/{m['losses']}",f(m['net_pnl_eur']),f(m['expectancy_eur']),f(m['mtm_drawdown_eur']),m['stops'],m['dispositions'].get('RIGHT_CENSORED',0)] for m in metrics if m['horizon_hours']==24])
newd+='''

Le signe dépend de l’horizon, de la taille et de l’occupation de capital. Certaines cellules24h sont positives ; elles ne permettent pas de choisir rétroactivement la variante ou la sortie gagnante. Aucun résultat hors échantillon n’est établi. Les sensibilités initiales interdisant les fills sur bougies sans transaction restent disponibles dans le pack ; elles ne validaient ni C1 ni C2.

### Premières entrées ciblées, disponibilité réellement prise en compte
'''
trs=[]
for name in ('F_Baseline','F_C1_range5','F_C2_v31','F_C3_revalidation'):
 es=list(csv.DictReader((OUT/f'trades_{name}_100_4h.csv').open()));seen=set()
 for e in es:
  if e['market'].split('-')[0] not in TARGETS or e['market'] in seen:continue
  seen.add(e['market'])
  if name=='F_C1_range5' and e['market']!='2Z-EUR':continue
  if name=='F_C3_revalidation' and e['source']!='REVALIDATION':continue
  trs.append([name,e['market'],time(e['entry_utc']),e['entry_eur'],f(float(e['risk_eur'])),f(float(e['mfe_horizon_pct'])),f(float(e['mae_horizon_pct'])),e['exit_reason'],f(float(e['pnl_eur']))])
newd+=table(['Variante','Actif','Entrée UTC','Prix €','Risque €','MFE %','MAE %','Sortie','PnL €'],trs)
newd+='''

Le premier RARE de la baseline touche son stop (−7,40 €/100), malgré sa hausse au snapshot. Le premier mail KMNO du21, hors fenêtre journal initiale, donne dans le test isolé une entrée02:55 à0,029940911 et un stop, soit−6,31 €/100 et−9,47 €/150. TREAD22 donne une entrée18:50 à0,47047, MFE+10,02 %, MAE−0,94 %, mais seulement+0,36 € au terme4h ;150 dépasse le risque12. QNT24 donne+7,32 €/100 ;150 est aussi refusé par le risque. KMNO24 donne−3,25 €/100 ; le glissement jusqu’à la bougie d’entrée fait également dépasser le risque12 à150. Ces contre-exemples empêchent d’assimiler « bon gagnant quotidien » à « bon trade à toute heure ».

### Ce qui est isolé et ce qui ne l’est pas

C1 isole le seuil range6→5 dans le sous-ensemble confirmé déjà testé. C2 mesure l’ajout d’une route qualifiée entière, pas un gate unique. C3 mesure la reprise de validations après rejet avec contrôle de thèse conservé. L’override volume petite taille ne peut pas être chiffré complètement faute de profondeur bid ; aucun uplift de spread/stop relâché n’est inventé. La réduction du montant est distincte d’une amélioration de signal.
'''
start=report.index('## D. Baseline vs challengers causaux');end=report.index('## E. Shadow test prospectif',start);report=report[:start]+newd+'\n\n'+report[end:]
report=report.replace('C3 SMALL_SIZE séparément','C3 revalidation et C4 SMALL_SIZE séparément')
report=report.replace('**Premier prix exécutable des mails prioritaires :**','**Premier prix exécutable des mails prioritaires, sous réserve de disponibilité de l’email :**')
report=report.replace('Un état DL immédiat n’est pas non plus une validation d’exécution complète.','Un état DL immédiat n’est pas non plus une validation d’exécution complète. De même, le terme fully_actionable du suivi de rejets n’intègre pas le prior thesis.')
report=report.replace('Corriger séparément l’évaluateur :','Ajouter au protocole shadow un registre des refus réévaluables ; publier un changement d’état EXÉCUTION_REVALIDÉE avec son heure de disponibilité, puis appliquer les mêmes protections de thèse, risque et données. C3 ne justifie pas encore de convertir systématiquement ces changements en recommandations d’achat.\n\nCorriger séparément l’évaluateur :')
report=report.replace('## Sources et reproductibilité','''## Attribution finale des faux négatifs

- **Faux négatif de détection :** non établi sur les dix ; l’absence de BUY ne l’implique pas.
- **Faux négatif d’envoi après premier PASS :** réfuté pour QNT/KMNO/TREAD et corrigé pour RARE. Leur email existe ; la suite ne prouve pas un achat réalisé.
- **Erreur de restitution identifiable :** TREAD22, confusion flux de nouveaux candidats / thèse antérieure ; omission d’achats DL par un consommateur top3. Impact euro utilisateur non identifiable sans ordre et transcript complet.
- **Conditions devenues meilleures après rejet :** 2Z24 et RARE26 attestés ; pas de re-routage production de ces validations shadow. Le premier refus pouvait être correct. C3 montre que la réactivation ajoute aussi des perdants ; ces cas ne sont pas tous des faux négatifs économiques.
- **Gates conservateurs prouvés économiquement :** aucun relâchement global démontré supérieur. 2Z autour de5,95 % montre une opportunité mécaniquement plausible sous le seuil6 ; HFT/COW restent indéterminés faute de carnets, AMP redevient propre pendant BUILDING, RUNE reste non qualifié, AGI est censuré.
- **Responsabilité non attribuable :** lecture/ordre QNT et KMNO, prix d’exécution à150 sur les carnets non conservés, allocation V3.5 ancienne, totalité des omissions ChatGPT. Ces inconnues ne sont attribuées artificiellement à aucune couche.

## Sources et reproductibilité''')
(OUT/'Audit_Solaire_2026-09-27_FINAL.md').write_text(report)
# Preserve original table but use delivery availability for actionable production.
rows10=list(csv.DictReader((OUT/'Tableau_10_actifs.csv').open()));delivery={'QNT-EUR':'24 13:59:26 ; 69,091 €','KMNO-EUR':'21 02:52:35 ; 0,029925 €','TREAD-EUR':'21 10:05:02 ; 0,38501 €','RARE-EUR':'25 21:32:50 ; 0,014528 €'}
for r in rows10:
 if r['Actif'] in delivery:
  r['Premier PASS production']='Résultat disponible au mail '+delivery[r['Actif']];r['Première décision actionable']='Production connue au mail '+delivery[r['Actif']]
 if r['Actif']=='2Z-EUR':r['Cause exacte / couche']+=' ; revalidation shadow publiée24/09 16:55:25, sans BUY ; C3 ajoute un trade100 perdant.'
 if r['Actif']=='RARE-EUR':r['Cause exacte / couche']+=' ; nouveau PASS revalidation publié26/09 17:53:32.'
csvout('Tableau_10_actifs_FINAL',rows10)
# Keep inline master table consistent with corrected standalone table.
a=report.index('| Actif | +24 h');b=report.index('\n\nLa table conserve',a);report=report[:a]+table(list(rows10[0]),[list(r.values()) for r in rows10])+report[b:]
(OUT/'Audit_Solaire_2026-09-27_FINAL.md').write_text(report)
print('final_chars',len(report),'bytes',len(report.encode()))
