# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T11:54:15.593934+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.995 | entrée 7.400 | trend 8.100 | rang 6.941
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.941

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 8.087/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.360/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.281/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources V4 — WATCH_ONLY
- AVA-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.940/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +107.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +32.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +21.40% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DGB-EUR +17.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +16.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HNT-EUR +13.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +13.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +12.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +12.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
