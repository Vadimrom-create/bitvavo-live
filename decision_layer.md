# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-10T06:28:01.348056+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.952 | entrée 6.000 | trend 8.750 | rang 7.038
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.731 | entrée 6.200 | trend 8.900 | rang 7.563
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.563
2. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.420
3. EDU-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.157

## Accélération indépendante

- LPT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — CONFIRMED_ACCELERATION — score 8.600/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.350/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — BUILDING_ACCELERATION — score 4.848/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — BUILDING_ACCELERATION — score 4.782/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — BUILDING_ACCELERATION — score 4.770/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LPT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CELR-EUR — MEMORY_24H — score mémoire 9.531/10 — sources ACCELERATION — MEMORY_ONLY
- OP-EUR — MEMORY_24H — score mémoire 9.301/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 9.136/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.114/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — ACTIVE_NOW — score mémoire 8.600/10 — sources ACCELERATION — WATCH_ONLY
- O-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 8.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.136/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- MAGIC-EUR +126.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAIA-EUR +52.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +32.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +24.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LPT-EUR +20.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PIXEL-EUR +20.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +19.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRV-EUR +18.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +17.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +14.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
