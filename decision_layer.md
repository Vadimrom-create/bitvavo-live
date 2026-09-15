# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T11:35:21.070279+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.363 | entrée 6.950 | trend 7.750 | rang 7.137
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.137
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.029
3. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.937

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.605/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +35.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PUFFER-EUR +26.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +20.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +17.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +17.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +13.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +10.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +8.26% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +7.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
