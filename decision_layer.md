# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T05:56:11.156556+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.762 | entrée 5.050 | trend 9.200 | rang 7.178
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.178
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.105
3. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.693

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.701/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.141/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +35.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +33.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +25.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CTR-EUR +9.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZRC-EUR +8.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +8.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +6.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PENDLE-EUR +6.59% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
