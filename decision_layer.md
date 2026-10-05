# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T12:55:20.827920+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ORCA-EUR | action ACHETE_MAINTENANT | opportunité 9.077 | entrée 6.900 | trend 8.650 | rang 8.234
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : YGG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.910 | entrée 6.150 | trend 8.450 | rang 7.718
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 7.527 | entrée 5.750 | trend 8.950 | rang 7.498
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.317 | entrée 7.050 | trend 8.900 | rang 8.219
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ORCA-EUR — ACHETE_MAINTENANT — rank 8.234 — opportunité 9.077 — entrée 6.900 — trend 8.650
2. QNT-EUR — ACHETE_MAINTENANT — rank 7.793 — opportunité 8.971 — entrée 7.500 — trend 7.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ORCA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.234
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.219
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.103

## Accélération indépendante

- GTC-EUR — BUILDING_ACCELERATION — score 6.318/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.775/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DIA-EUR — BUILDING_ACCELERATION — score 5.623/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.381/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEX-EUR — BUILDING_ACCELERATION — score 5.107/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.058/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 4.873/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_DECAY_24_72H — score mémoire 9.090/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PLUME-EUR — MEMORY_24H — score mémoire 8.672/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.392/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +78.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +63.48% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RLC-EUR +54.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +28.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +19.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +14.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +12.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UMA-EUR +11.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +11.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ADA-EUR +11.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
