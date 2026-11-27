# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-27T20:24:48.342405+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.994 | entrée 7.200 | trend 7.900 | rang 6.879
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.879
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.659
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.621

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 7.461/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THE-EUR — CONFIRMED_ACCELERATION — score 6.658/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — BUILDING_ACCELERATION — score 5.536/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SLX-EUR — BUILDING_ACCELERATION — score 4.773/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 4.761/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.613/10 — sources ACCELERATION — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 7.461/10 — sources ACCELERATION — WATCH_ONLY
- O-EUR — ACTIVE_NOW — score mémoire 7.422/10 — sources V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.275/10 — sources ACCELERATION — MEMORY_ONLY
- KNTQ-EUR — MEMORY_DECAY_24_72H — score mémoire 7.128/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.879/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_DECAY_24_72H — score mémoire 6.833/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.826/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 6.659/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY

## Audit des plus fortes hausses

- PORTAL-EUR +216.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THE-EUR +39.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +26.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +25.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +17.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LISTA-EUR +14.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +12.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CFG-EUR +10.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +10.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +9.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
