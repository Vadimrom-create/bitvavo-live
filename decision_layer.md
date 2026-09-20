# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:31:36.097445+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.254 | entrée 7.350 | trend 8.500 | rang 7.888
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PEAQ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.171 | entrée 5.950 | trend 8.350 | rang 7.440
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.630 | entrée 5.650 | trend 8.300 | rang 7.354
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.154 | entrée 6.750 | trend 8.200 | rang 8.200
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.200
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952
3. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.888

## Accélération indépendante

- SKL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.854/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.399/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MMT-EUR — BUILDING_ACCELERATION — score 5.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.346/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.297/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.857/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources V4 — BUYABLE_NOW
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SKL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +51.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +26.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +25.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +22.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +18.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +17.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +16.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +14.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +14.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
