# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T02:01:41.353406+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.205 | entrée 7.200 | trend 8.750 | rang 7.989
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.799 | entrée 6.050 | trend 8.200 | rang 7.965
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 8.548 | entrée 4.900 | trend 8.950 | rang 7.982
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.924 | entrée 7.150 | trend 8.950 | rang 7.915
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.989 — opportunité 8.205 — entrée 7.200 — trend 8.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.989
2. FLUX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.982
3. APE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.965

## Accélération indépendante

- IRYS-EUR — BUILDING_ACCELERATION — score 6.264/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APE-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +43.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +30.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +30.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +27.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +23.02% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- INX-EUR +17.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +15.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +15.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRUST-EUR +11.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- IMX-EUR +11.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
