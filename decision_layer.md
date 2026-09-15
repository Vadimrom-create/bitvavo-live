# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T07:25:52.917384+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.425 | entrée 6.650 | trend 8.100 | rang 7.250
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.250
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.228
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.197

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — MEMORY_24H — score mémoire 7.747/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.651/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.535/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.529/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +28.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +26.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +21.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +13.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +11.11% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +9.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +8.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +7.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AXL-EUR +6.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
