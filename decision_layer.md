# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T15:47:40.432696+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.291 | entrée 7.400 | trend 8.050 | rang 7.766
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : THE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.667 | entrée 6.450 | trend 8.700 | rang 7.648
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BREV-EUR | action LATENT_ACCELERATOR | opportunité 7.586 | entrée 4.500 | trend 8.450 | rang 7.282
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.617 | entrée 6.350 | trend 8.850 | rang 7.987
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.987
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.882
3. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.766

## Accélération indépendante

- MLN-EUR — CONFIRMED_ACCELERATION — score 9.132/10 — DETECTED_BUT_TOO_LATE
- ETC-EUR — CONFIRMED_ACCELERATION — score 8.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — CONFIRMED_ACCELERATION — score 7.517/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — CONFIRMED_ACCELERATION — score 7.386/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 6.359/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.261/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 6.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.863/10 — DETECTED_BUT_TOO_LATE
- AEVO-EUR — BUILDING_ACCELERATION — score 5.512/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 6.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MLN-EUR — ACTIVE_NOW — score mémoire 9.132/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.987/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +90.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FLOCK-EUR +33.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +27.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +24.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +16.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CHR-EUR +15.60% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KITE-EUR +15.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +14.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +13.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
