# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T07:47:49.409609+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.942 | entrée 7.000 | trend 8.100 | rang 6.798
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.798

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.227/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources V4 — DETECTED_BUT_TOO_LATE
- COTI-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MASK-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +68.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +29.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +24.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +19.56% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +15.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +13.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +13.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +13.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
