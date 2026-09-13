# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T13:13:12.457954+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.690 | entrée 4.500 | trend 9.200 | rang 6.808
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.895 | entrée 7.350 | trend 8.650 | rang 7.835
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.835
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.458
3. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.808

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.253/10 — sources V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.210/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.916/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AKT-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +334.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +68.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +40.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +23.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +21.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRAX-EUR +17.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +17.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVA-EUR +16.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- WAXP-EUR +15.72% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KNC-EUR +14.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
