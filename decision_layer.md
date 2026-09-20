# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T17:26:23.784997+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.554 | entrée 7.850 | trend 7.700 | rang 7.806
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.475 | entrée 4.500 | trend 8.300 | rang 7.087
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.948 | entrée 6.250 | trend 8.500 | rang 7.036
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.806
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.591
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.425

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.349/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 7.188/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.802/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 4.835/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.425/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- STX-EUR — ACTIVE_NOW — score mémoire 8.003/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.803/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +54.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +40.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +26.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +26.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +18.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LUNA2-EUR +18.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +16.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +15.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +14.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +14.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
