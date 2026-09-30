# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T13:24:00.850553+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.130 | entrée 7.800 | trend 8.700 | rang 8.353
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.167 | entrée 5.900 | trend 8.500 | rang 7.595
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 8.013 | entrée 4.500 | trend 9.000 | rang 7.686
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.444 | entrée 6.750 | trend 8.900 | rang 8.423
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.353 — opportunité 9.130 — entrée 7.800 — trend 8.700
2. XLM-EUR — ACHETE_MAINTENANT — rank 8.238 — opportunité 8.672 — entrée 7.850 — trend 8.700
3. ICP-EUR — ACHETE_MAINTENANT — rank 8.136 — opportunité 8.590 — entrée 6.950 — trend 9.200
4. ETHFI-EUR — ACHETE_MAINTENANT — rank 8.110 — opportunité 8.932 — entrée 6.950 — trend 8.650
5. WIF-EUR — ACHETE_MAINTENANT — rank 8.004 — opportunité 9.189 — entrée 7.400 — trend 7.800
6. AVAX-EUR — ACHETE_MAINTENANT — rank 7.934 — opportunité 8.417 — entrée 7.150 — trend 8.450
7. FET-EUR — ACHETE_MAINTENANT — rank 7.853 — opportunité 9.061 — entrée 7.400 — trend 7.900
8. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.845 — opportunité 8.587 — entrée 6.950 — trend 8.450
9. GALA-EUR — ACHETE_MAINTENANT — rank 7.836 — opportunité 8.431 — entrée 6.850 — trend 8.400
10. RENDER-EUR — ACHETE_MAINTENANT — rank 7.761 — opportunité 8.213 — entrée 7.350 — trend 8.400
11. NEAR-EUR — ACHETE_MAINTENANT — rank 7.733 — opportunité 8.843 — entrée 7.250 — trend 7.750
12. ONDO-EUR — ACHETE_MAINTENANT — rank 7.724 — opportunité 8.934 — entrée 6.950 — trend 7.900
13. TAO-EUR — ACHETE_MAINTENANT — rank 7.647 — opportunité 8.576 — entrée 7.400 — trend 7.700
14. SUI-EUR — ACHETE_MAINTENANT — rank 7.613 — opportunité 8.492 — entrée 7.200 — trend 7.900
15. ADA-EUR — ACHETE_MAINTENANT — rank 7.466 — opportunité 8.868 — entrée 7.600 — trend 7.100
16. SOL-EUR — ACHETE_MAINTENANT — rank 7.445 — opportunité 8.962 — entrée 7.350 — trend 6.800
17. DOGE-EUR — ACHETE_MAINTENANT — rank 7.345 — opportunité 8.832 — entrée 7.250 — trend 6.600
18. POL-EUR — ACHETE_MAINTENANT — rank 7.329 — opportunité 7.902 — entrée 6.900 — trend 7.950
19. ETC-EUR — ACHETE_MAINTENANT — rank 7.256 — opportunité 8.525 — entrée 6.800 — trend 6.950
20. PEPE-EUR — ACHETE_MAINTENANT — rank 6.880 — opportunité 8.697 — entrée 7.650 — trend 5.650
21. FLOKI-EUR — ACHETE_MAINTENANT — rank 6.423 — opportunité 8.318 — entrée 6.800 — trend 5.350
22. ENA-EUR — ACHETE_MAINTENANT — rank 6.197 — opportunité 7.564 — entrée 6.800 — trend 5.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.423
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.353
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.238

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 9.770/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — CONFIRMED_ACCELERATION — score 7.946/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.637/10 — DETECTED_BUT_TOO_LATE
- ZKC-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 6.029/10 — DETECTED_BUT_TOO_LATE
- FIDA-EUR — BUILDING_ACCELERATION — score 5.542/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 5.284/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 5.282/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 5.255/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SOON-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOM-EUR — ACTIVE_NOW — score mémoire 9.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.688/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ARK-EUR +56.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +54.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +41.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +34.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +16.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +15.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +15.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +14.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +14.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +12.62% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
