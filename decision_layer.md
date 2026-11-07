# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-07T08:44:16.254127+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : NES-EUR | action LATENT_ACCELERATOR | opportunité 7.526 | entrée 4.800 | trend 8.650 | rang 7.125
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BIRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.790 | entrée 5.250 | trend 8.300 | rang 6.566
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NES-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.125
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.566
3. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.540

## Accélération indépendante

- BOB-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — CONFIRMED_ACCELERATION — score 7.602/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.498/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACT-EUR — BUILDING_ACCELERATION — score 6.303/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — BUILDING_ACCELERATION — score 4.949/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 4.757/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION — MEMORY_ONLY
- CARV-EUR — MEMORY_24H — score mémoire 9.061/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.929/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — WATCH_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.439/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.068/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PTB-EUR — MEMORY_DECAY_24_72H — score mémoire 7.484/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 7.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +39.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +24.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +22.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +17.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +10.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +10.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +10.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +10.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +7.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SWELL-EUR +7.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
