# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T11:41:52.761296+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.242 | entrée 7.000 | trend 8.700 | rang 7.924
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.065 | entrée 6.650 | trend 7.400 | rang 7.633
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LRC-EUR | action LATENT_ACCELERATOR | opportunité 7.877 | entrée 5.650 | trend 8.000 | rang 7.241
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.322 | entrée 6.700 | trend 8.650 | rang 7.904
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 7.924 — opportunité 8.242 — entrée 7.000 — trend 8.700
2. LTC-EUR — ACHETE_MAINTENANT — rank 7.635 — opportunité 8.033 — entrée 7.650 — trend 8.150
3. SEI-EUR — ACHETE_MAINTENANT — rank 7.600 — opportunité 8.024 — entrée 7.500 — trend 8.600
4. LINK-EUR — ACHETE_MAINTENANT — rank 7.259 — opportunité 8.087 — entrée 7.150 — trend 7.250
5. PUMP-EUR — ACHETE_MAINTENANT — rank 6.583 — opportunité 8.046 — entrée 7.000 — trend 6.550
6. ETH-EUR — ACHETE_MAINTENANT — rank 6.470 — opportunité 8.420 — entrée 7.600 — trend 4.650
7. HYPE-EUR — ACHETE_MAINTENANT — rank 6.375 — opportunité 8.065 — entrée 7.350 — trend 4.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.924
2. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.904
3. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.876

## Accélération indépendante

- NMR-EUR — CONFIRMED_ACCELERATION — score 9.777/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — CONFIRMED_ACCELERATION — score 7.118/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — CONFIRMED_ACCELERATION — score 6.990/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.438/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALGO-EUR — BUILDING_ACCELERATION — score 5.357/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.141/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — BUILDING_ACCELERATION — score 4.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LINK-EUR — ACTIVE_NOW — score mémoire 7.259/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NMR-EUR — ACTIVE_NOW — score mémoire 9.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +53.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +24.29% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +16.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +15.26% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- GRT-EUR +14.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +12.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +11.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +11.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +10.92% — DETECTED_EARLY — couche NONE — action NONE
- XDC-EUR +9.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
