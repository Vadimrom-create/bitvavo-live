# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-27T11:44:23.601918+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.371 | entrée 6.050 | trend 7.900 | rang 6.963
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.963
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.573
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.455

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 9.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PORTAL-EUR — CONFIRMED_ACCELERATION — score 7.613/10 — DETECTED_BUT_TOO_LATE
- AXIS-EUR — CONFIRMED_ACCELERATION — score 6.826/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.665/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.569/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XVG-EUR — BUILDING_ACCELERATION — score 5.517/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MMT-EUR — BUILDING_ACCELERATION — score 5.031/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 4.816/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — ACTIVE_NOW — score mémoire 9.317/10 — sources ACCELERATION — WATCH_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.613/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CSPR-EUR — MEMORY_24H — score mémoire 7.291/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.266/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 7.199/10 — sources V4 — MEMORY_ONLY
- AIXBT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.173/10 — sources ACCELERATION — MEMORY_ONLY
- KNTQ-EUR — MEMORY_24H — score mémoire 7.144/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 6.848/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — ACTIVE_NOW — score mémoire 6.826/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PORTAL-EUR +88.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KNTQ-EUR +39.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +38.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +21.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CFG-EUR +20.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FET-EUR +11.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- REZ-EUR +11.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +9.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LISTA-EUR +9.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +9.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
