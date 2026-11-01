# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-01T22:47:02.686794+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.434 | entrée 5.300 | trend 8.450 | rang 7.158
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.158
2. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.931
3. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.783

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 9.840/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 8.693/10 — sources ACCELERATION — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 8.642/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.280/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 8.114/10 — sources ACCELERATION — MEMORY_ONLY
- STO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.435/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.363/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.158/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.949/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 6.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +12.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLOCK-EUR +11.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- G-EUR +10.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +8.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUMP-EUR +7.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KITE-EUR +6.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BEAM-EUR +6.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +5.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WHUF-EUR +5.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POWR-EUR +5.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
