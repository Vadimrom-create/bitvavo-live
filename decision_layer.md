# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-08T08:56:33.682487+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TRUST-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.944 | entrée 5.150 | trend 8.100 | rang 6.716
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.716
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.596
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.314

## Accélération indépendante

- WHUF-EUR — CONFIRMED_ACCELERATION — score 8.877/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAT-EUR — BUILDING_ACCELERATION — score 5.607/10 — DETECTED_BUT_TOO_LATE
- SAFE-EUR — BUILDING_ACCELERATION — score 5.604/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOT-EUR — BUILDING_ACCELERATION — score 5.385/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 9.403/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — ACTIVE_NOW — score mémoire 8.877/10 — sources ACCELERATION — WATCH_ONLY
- BOB-EUR — MEMORY_DECAY_24_72H — score mémoire 8.464/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources ACCELERATION — WATCH_ONLY
- CARV-EUR — MEMORY_DECAY_24_72H — score mémoire 7.772/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_DECAY_24_72H — score mémoire 7.659/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.570/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 7.095/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — MEMORY_24H — score mémoire 7.048/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BLEND-EUR — MEMORY_24H — score mémoire 6.827/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +26.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HMSTR-EUR +8.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +7.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SWELL-EUR +7.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +7.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +6.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +6.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DGB-EUR +5.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +4.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SAFE-EUR +4.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
