# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T14:50:55.854692+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.780 | entrée 4.700 | trend 9.200 | rang 7.695
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SYRUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.433 | entrée 6.400 | trend 7.950 | rang 7.490
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.695
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.490
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.435

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 9.912/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVA-EUR — ACTIVE_NOW — score mémoire 9.912/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YGG-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.695/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +106.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +21.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +21.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +20.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +19.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDEN-EUR +18.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +18.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +17.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +16.84% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
