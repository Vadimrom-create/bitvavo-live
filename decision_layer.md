# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T03:22:53.595628+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.646 | entrée 6.250 | trend 8.650 | rang 7.621
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 8.002 | entrée 5.550 | trend 8.950 | rang 7.773
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.049 | entrée 6.350 | trend 8.950 | rang 7.884
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.884
2. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.860
3. FLUX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.773

## Accélération indépendante

- AUDIO-EUR — BUILDING_ACCELERATION — score 5.727/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — BUILDING_ACCELERATION — score 4.926/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — BUILDING_ACCELERATION — score 4.830/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — BUILDING_ACCELERATION — score 4.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 4.804/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 7.686/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TURBO-EUR — MEMORY_24H — score mémoire 7.669/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +50.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +33.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IRYS-EUR +21.45% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRT-EUR +18.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +16.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +16.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +15.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +15.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +13.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +11.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
