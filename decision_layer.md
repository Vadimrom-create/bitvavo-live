# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T05:21:00.277652+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.478 | entrée 6.350 | trend 7.750 | rang 7.040
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.040

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.058/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.323/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.635/10 — sources V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.627/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +40.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +32.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTR-EUR +11.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +9.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +8.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +7.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- OP-EUR +6.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +6.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
