# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T06:28:52.015593+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.776 | entrée 7.200 | trend 8.700 | rang 8.043
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.449 | entrée 6.100 | trend 8.200 | rang 7.290
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 8.413 | entrée 5.750 | trend 8.650 | rang 7.477
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.986 | entrée 6.250 | trend 8.650 | rang 7.718
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 8.043 — opportunité 8.776 — entrée 7.200 — trend 8.700
2. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.956 — opportunité 8.363 — entrée 6.900 — trend 8.750
3. LTC-EUR — ACHETE_MAINTENANT — rank 7.660 — opportunité 7.920 — entrée 7.250 — trend 8.150
4. HBAR-EUR — ACHETE_MAINTENANT — rank 6.885 — opportunité 7.432 — entrée 7.200 — trend 7.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.043
2. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.956
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.718

## Accélération indépendante

- IKA-EUR — BUILDING_ACCELERATION — score 6.065/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.415/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 4.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.828/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +51.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +43.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +22.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +16.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +14.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +13.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +13.71% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- WMTX-EUR +11.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +11.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +11.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
