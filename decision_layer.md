# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T16:23:41.720970+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 9.227 | entrée 7.600 | trend 7.900 | rang 7.987
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.024 | entrée 5.950 | trend 9.000 | rang 7.872
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 8.697 | entrée 5.650 | trend 8.200 | rang 7.779
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.246 | entrée 7.350 | trend 9.200 | rang 8.374
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SUI-EUR — ACHETE_MAINTENANT — rank 7.987 — opportunité 9.227 — entrée 7.600 — trend 7.900
2. DOT-EUR — ACHETE_MAINTENANT — rank 7.737 — opportunité 8.457 — entrée 7.000 — trend 7.950
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.658 — opportunité 8.490 — entrée 6.950 — trend 7.750
4. XDC-EUR — ACHETE_MAINTENANT — rank 7.644 — opportunité 7.819 — entrée 7.550 — trend 8.200
5. PUMP-EUR — ACHETE_MAINTENANT — rank 7.472 — opportunité 8.121 — entrée 7.150 — trend 8.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.374
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.181
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.136

## Accélération indépendante

- SUSHI-EUR — CONFIRMED_ACCELERATION — score 9.203/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 8.839/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — CONFIRMED_ACCELERATION — score 7.178/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.118/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — CONFIRMED_ACCELERATION — score 6.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALT-EUR — CONFIRMED_ACCELERATION — score 6.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — CONFIRMED_ACCELERATION — score 6.518/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.495/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 6.357/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.987/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.658/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SUSHI-EUR — ACTIVE_NOW — score mémoire 9.203/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DEEP-EUR — ACTIVE_NOW — score mémoire 8.839/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.615/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +58.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +44.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +31.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +23.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +22.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +18.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +17.25% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +16.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +15.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MERL-EUR +14.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
