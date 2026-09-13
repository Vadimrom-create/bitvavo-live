# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T22:44:44.452379+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.638 | entrée 4.950 | trend 9.200 | rang 6.735
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.963 | entrée 6.750 | trend 8.650 | rang 7.827
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.827
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.023
3. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.735

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.544/10 — sources V4 — DETECTED_BUT_TOO_LATE
- WLD-EUR — ACTIVE_NOW — score mémoire 7.489/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.468/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +270.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +50.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +24.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +18.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +16.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +14.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +13.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +11.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +10.96% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XTZ-EUR +8.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
