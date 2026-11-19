# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-19T02:12:28.668872+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : DODO-EUR | action LATENT_ACCELERATOR | opportunité 8.259 | entrée 5.750 | trend 8.650 | rang 7.649
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MEGA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.474 | entrée 7.200 | trend 8.350 | rang 6.971
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.649
2. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.971
3. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 4.990

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.201/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 5.504/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 5.338/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLEND-EUR — BUILDING_ACCELERATION — score 5.017/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TOWNS-EUR — MEMORY_24H — score mémoire 9.889/10 — sources ACCELERATION — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.871/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 7.650/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 7.201/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — ACTIVE_NOW — score mémoire 7.000/10 — sources ACCELERATION — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 6.971/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HMSTR-EUR — MEMORY_24H — score mémoire 6.740/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 6.679/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 6.602/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +66.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +52.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CROSS-EUR +26.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +21.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +20.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +18.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +16.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +15.94% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WHUF-EUR +15.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKC-EUR +13.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
