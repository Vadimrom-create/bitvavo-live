# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T09:58:53.307890+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CC-EUR | action ACHETE_MAINTENANT | opportunité 9.220 | entrée 7.200 | trend 8.700 | rang 8.175
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.926 | entrée 6.550 | trend 7.300 | rang 7.557
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.673 | entrée 5.200 | trend 8.400 | rang 7.878
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUPER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.157 | entrée 6.500 | trend 8.050 | rang 7.950
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CC-EUR — ACHETE_MAINTENANT — rank 8.175 — opportunité 9.220 — entrée 7.200 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.175
2. SUPER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.950
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.915

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CC-EUR — ACTIVE_NOW — score mémoire 8.175/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GRAM-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +20.55% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +17.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +13.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +11.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +11.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +7.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +7.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +6.18% — DETECTED_EARLY — couche NONE — action NONE
- SOSO-EUR +5.82% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CAP-EUR +5.81% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
