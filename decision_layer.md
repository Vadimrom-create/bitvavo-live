# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T21:17:07.871833+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.009 | entrée 6.250 | trend 8.100 | rang 7.256
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.256
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.190

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.104/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.428/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 9.104/10 — sources ACCELERATION — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.392/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.361/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.258/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.130/10 — sources V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +127.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +96.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +31.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +21.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +19.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +16.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +14.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +14.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +11.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +11.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
