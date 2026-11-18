# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-18T12:30:18.768768+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.385 | entrée 6.300 | trend 8.500 | rang 7.273
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.273
2. HMSTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.740
3. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.534

## Accélération indépendante

- SWELL-EUR — CONFIRMED_ACCELERATION — score 7.650/10 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — BUILDING_ACCELERATION — score 6.009/10 — DETECTED_BUT_TOO_LATE
- CARV-EUR — BUILDING_ACCELERATION — score 5.946/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXIS-EUR — BUILDING_ACCELERATION — score 5.506/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_24H — score mémoire 9.871/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 7.896/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — ACTIVE_NOW — score mémoire 7.650/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DODO-EUR — ACTIVE_NOW — score mémoire 7.273/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.101/10 — sources V4 — WATCH_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.033/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.803/10 — sources ACCELERATION — MEMORY_ONLY
- HMSTR-EUR — ACTIVE_NOW — score mémoire 6.740/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 6.679/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.534/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MMT-EUR +105.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BREV-EUR +52.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +35.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +30.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKC-EUR +24.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +18.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WHUF-EUR +16.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOCA-EUR +14.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +14.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +12.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
