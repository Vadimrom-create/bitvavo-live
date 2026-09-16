# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T03:41:10.814462+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.976 | entrée 6.900 | trend 8.100 | rang 7.169
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.169
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.798

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.720/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.678/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.663/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.658/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +35.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +27.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +25.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +22.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +20.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUFFER-EUR +16.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +15.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +13.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +12.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +11.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
