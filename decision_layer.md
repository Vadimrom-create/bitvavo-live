# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T09:41:54.732585+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.705 | entrée 6.400 | trend 8.650 | rang 7.643
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.653 | entrée 5.750 | trend 9.200 | rang 7.693
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.693
2. VET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.643
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.082

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.693/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.643/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.609/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +52.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +42.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +25.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +25.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +22.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +18.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +13.28% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +10.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +9.49% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MTL-EUR +8.46% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
