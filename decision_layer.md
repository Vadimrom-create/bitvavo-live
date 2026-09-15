# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T09:03:56.236785+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.752 | entrée 6.050 | trend 9.200 | rang 7.844
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.844
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.599
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.412

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 7.083/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.048/10 — DETECTED_BUT_TOO_LATE
- PUNDIX-EUR — BUILDING_ACCELERATION — score 4.898/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.599/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +34.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +26.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +22.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +21.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +13.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XMN-EUR +11.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +10.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +9.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +9.74% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
