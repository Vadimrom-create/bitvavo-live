# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T11:21:08.193973+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 7.900 | trend 8.150 | rang 8.271
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.830 | entrée 6.100 | trend 7.400 | rang 7.534
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NMR-EUR | action LATENT_ACCELERATOR | opportunité 7.879 | entrée 5.400 | trend 8.150 | rang 6.989
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.199 | entrée 6.750 | trend 8.750 | rang 7.803
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LTC-EUR — ACHETE_MAINTENANT — rank 8.271 — opportunité 9.284 — entrée 7.900 — trend 8.150
2. KAS-EUR — ACHETE_MAINTENANT — rank 7.843 — opportunité 8.053 — entrée 6.900 — trend 8.700
3. LINK-EUR — ACHETE_MAINTENANT — rank 7.232 — opportunité 8.048 — entrée 6.900 — trend 7.250

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.271
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.843
3. GRAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.803

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 9.575/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — CONFIRMED_ACCELERATION — score 8.655/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 8.319/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — CONFIRMED_ACCELERATION — score 8.096/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 6.117/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZETA-EUR — BUILDING_ACCELERATION — score 5.924/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 4.956/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LINK-EUR — ACTIVE_NOW — score mémoire 7.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — ACTIVE_NOW — score mémoire 9.575/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IKA-EUR — ACTIVE_NOW — score mémoire 8.655/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +48.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +21.82% — DETECTED_EARLY — couche NONE — action NONE
- AUDIO-EUR +13.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +13.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +11.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +10.60% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PUMP-EUR +10.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +9.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +9.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +8.52% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
