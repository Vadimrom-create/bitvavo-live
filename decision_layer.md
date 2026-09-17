# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T15:06:19.443045+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.968 | entrée 5.500 | trend 9.200 | rang 7.875
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.667 | entrée 6.750 | trend 7.950 | rang 7.749
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.875
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.749
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.064

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 7.438/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.697/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — MEMORY_24H — score mémoire 7.671/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +103.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +36.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +23.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +20.44% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +20.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +18.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +18.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDEN-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +17.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +17.37% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
