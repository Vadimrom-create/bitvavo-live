# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T11:29:13.014991+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.305 | entrée 8.050 | trend 8.500 | rang 8.371
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.419 | entrée 6.050 | trend 8.700 | rang 7.843
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 8.117 | entrée 4.500 | trend 8.950 | rang 7.669
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XLM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.422 | entrée 8.150 | trend 8.750 | rang 8.221
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.371
2. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.221
3. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.206

## Accélération indépendante

- ENA-EUR — CONFIRMED_ACCELERATION — score 9.131/10 — DETECTED_BUT_TOO_LATE
- SUI-EUR — CONFIRMED_ACCELERATION — score 8.655/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — CONFIRMED_ACCELERATION — score 8.360/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.963/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.962/10 — DETECTED_BUT_TOO_LATE
- C98-EUR — BUILDING_ACCELERATION — score 6.399/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.282/10 — DETECTED_BUT_TOO_LATE
- KAS-EUR — BUILDING_ACCELERATION — score 6.242/10 — DETECTED_BUT_TOO_LATE
- AKT-EUR — BUILDING_ACCELERATION — score 6.196/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 6.173/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RENDER-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ENA-EUR — ACTIVE_NOW — score mémoire 9.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.655/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.371/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.360/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- TREAD-EUR +43.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +40.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +35.02% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +29.51% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +28.73% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +27.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +21.37% — DETECTED_EARLY — couche NONE — action NONE
- DEEP-EUR +20.54% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEAQ-EUR +20.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
