# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-14T00:00:29.770372+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.703 | entrée 7.050 | trend 8.850 | rang 7.594
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.594
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.705
3. SXT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.517

## Accélération indépendante

- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.598/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZEUS-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DODO-EUR — ACTIVE_NOW — score mémoire 7.594/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 7.492/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.417/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 6.767/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 6.705/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 6.517/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 6.485/10 — sources DECISION_LAYER — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.478/10 — sources V4 — MEMORY_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 6.209/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SHELL-EUR +84.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +20.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +10.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INJ-EUR +9.12% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BILL-EUR +7.25% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SLX-EUR +6.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STO-EUR +6.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +6.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GMX-EUR +6.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HMSTR-EUR +6.12% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
