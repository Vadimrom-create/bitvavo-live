# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T06:52:32.201712+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.436 | entrée 6.950 | trend 6.450 | rang 7.067
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XDC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.453 | entrée 6.500 | trend 7.550 | rang 7.022
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.919 | entrée 5.350 | trend 8.450 | rang 7.536
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SKY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.642 | entrée 6.650 | trend 8.450 | rang 7.971
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LTC-EUR — ACHETE_MAINTENANT — rank 7.067 — opportunité 8.436 — entrée 6.950 — trend 6.450
2. CRV-EUR — ACHETE_MAINTENANT — rank 6.222 — opportunité 8.082 — entrée 6.800 — trend 6.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.971
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.924
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.871

## Accélération indépendante

- GMT-EUR — CONFIRMED_ACCELERATION — score 9.050/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — CONFIRMED_ACCELERATION — score 7.805/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 5.781/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 5.575/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — BUILDING_ACCELERATION — score 5.356/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.122/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.089/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — BUILDING_ACCELERATION — score 4.903/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 4.781/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.616/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 9.050/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +61.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +19.04% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +14.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMX-EUR +13.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +13.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +9.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PIXEL-EUR +9.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AXS-EUR +8.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
