# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T07:02:39.860246+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.369 | entrée 7.350 | trend 8.100 | rang 7.284
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.284
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.270
3. POWR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.169

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.365/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.747/10 — sources V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.623/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +32.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +27.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +19.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AXL-EUR +13.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +12.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +10.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +8.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +7.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CTR-EUR +7.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
