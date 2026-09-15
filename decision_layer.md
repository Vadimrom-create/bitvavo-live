# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T17:20:38.864000+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.838 | entrée 5.550 | trend 9.200 | rang 7.677
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.632 | entrée 6.850 | trend 8.100 | rang 7.124
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.677
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.124
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.948

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 7.886/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.694/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.658/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.590/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +31.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +18.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NES-EUR +16.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +12.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +10.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +9.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +8.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +8.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
