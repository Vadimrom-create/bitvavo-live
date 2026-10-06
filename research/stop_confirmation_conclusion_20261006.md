# Conclusion — audit des sorties sur stop — 2026-10-06

## Portée

Analyse de 98 cas `BUY_SENT` historiques de Solaire ayant touché leur stop dans les 12 h, plus le cas manuel VTHO du 6 octobre. Aucun comportement de production n'est modifié par ce document.

## Constat principal

Le remplacement global de « stop touché => sortie » par une simple confirmation de clôture n'est pas suffisamment robuste.

Sur 99 cas de stop touché :
- 58 repassent au-dessus du stop à +60 min ;
- 47 repassent au-dessus du stop à +4 h ;
- mais attendre une confirmation fait aussi sortir de nombreux vrais perdants plus bas.

Les politiques universelles à clôture 5m / 2x5m / 15m améliorent la moyenne grâce à quelques gros sauvetages, mais leur médiane reste négative par rapport à la sortie au toucher.

## Cas VTHO

Référence :
- PRU/entrée de travail : 0,000678 € ;
- invalidation structurelle de référence : 0,00064761 € ;
- vente réelle : 0,000634 € ;
- le prix a clôturé sous l'invalidation, puis a récupéré au-dessus du stop en environ 60 min.

VTHO n'est donc pas un simple « wick only » au sens strict :
- la bougie 5m de l'exécution clôture à ~0,00063859 €, sous le stop ;
- le scénario touche aussi le niveau catastrophe 1,50R ;
- il ne touche pas 1,75R ;
- à +4 h, la clôture est ~0,00065901 €, soit +1,76 % au-dessus du stop.

Pour sauver exactement VTHO, il faut accepter une tolérance plus profonde (environ 1,75R, ou une confirmation matérialisée à ~0,5R sous le soft stop). Appliquer cette tolérance partout dégrade trop la queue de pertes.

## Signal discriminant utile : phase 1h à l'entrée

Sur les 98 cas historiques appariés :
- `PULLBACK_1H` : 26 stop-touches, seulement 9 récupérations à +60 min ; retarder la sortie avec 2 clôtures 5m / hard stop 1,75R détériore 25 cas sur 26, moyenne -0,68 point.
- `MIXED_1H` : 31 récupérations à +60 min sur 47 cas.
- `EXPANSION_1H` : 14 récupérations à +60 min sur 21 cas.

Le meilleur compromis testé devient donc conditionnel :
1. si la position a été ouverte en `PULLBACK_1H` (ou si la phase est inconnue) : conserver la sortie au stop structurel ;
2. si la position a été ouverte en `MIXED_1H` ou `EXPANSION_1H` : ne pas liquider au premier touch ; demander deux clôtures 5m consécutives sous le stop ;
3. conserver un hard stop catastrophe à 1,75R.

Sur les 98 cas historiques, cette règle conditionnelle donne, versus stop au toucher :
- moyenne : +0,963 point de rendement ;
- médiane : -0,014 point ;
- moyenne tronquée 5 % : +0,325 point ;
- 19 cas améliorés, 49 détériorés, 30 identiques (sortie immédiate en PULLBACK/phase inconnue) ;
- pire dégradation : -3,283 points ;
- meilleur sauvetage : +39,248 points.

La moyenne reste positive même en retirant les plus gros cas favorables dans les contrôles effectués. Ce résultat est nettement plus robuste que l'application universelle d'une confirmation retardée.

## Décision

Ne pas modifier immédiatement la production sur la seule base de VTHO.

Candidat à tester prospectivement en SHADOW :
`PHASE_AWARE_2X5M_HARD_1_75R`

- PULLBACK_1H / phase inconnue -> stop structurel immédiat.
- MIXED_1H / EXPANSION_1H -> 2 clôtures 5m sous le soft stop avant sortie.
- Hard stop catastrophe = 1,75R.
- Une éventuelle promotion en production devra conserver le même risque maximum en euros, donc adapter la taille si le hard stop est plus éloigné.

## Lacune de mesure identifiée

Le shadow historique `production_exit_policy_shadow` ne suit plus les emails d'achat issus du nouveau chemin direct : il lit seulement les `BUY_SENT` de `production_decision_journal.json`. Or les emails directs récents (dont VTHO) ne sont pas inscrits dans ce journal. Il faut corriger la journalisation des achats directs avant qu'un test prospectif puisse être considéré comme fiable.
