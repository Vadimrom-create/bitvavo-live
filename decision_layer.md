# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T13:21:02.035651+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : PEAQ-EUR | action LATENT_ACCELERATOR | opportunité 7.847 | entrée 5.650 | trend 8.550 | rang 6.663
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.455 | entrée 7.050 | trend 8.100 | rang 6.609
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEAQ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.663
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.609

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.468/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources V4 — DETECTED_BUT_TOO_LATE
- INJ-EUR — ACTIVE_NOW — score mémoire 7.628/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.614/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.585/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.582/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +95.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +30.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +19.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +18.78% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- FOLD-EUR +18.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +17.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDEN-EUR +16.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +14.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DGB-EUR +14.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
