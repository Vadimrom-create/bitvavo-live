# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T16:35:47.012392+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.131 | entrée 5.600 | trend 9.200 | rang 7.964
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.964
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.230

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 8.337/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.150/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.859/10 — sources V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +36.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +35.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +27.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +16.63% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +14.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +13.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +12.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RON-EUR +10.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +9.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SENT-EUR +9.07% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
