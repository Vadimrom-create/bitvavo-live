# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-25T09:33:29.849444+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.015 | entrée 5.400 | trend 8.200 | rang 6.777
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.777
2. AI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.231
3. TREAD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.158

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_DECAY_24_72H — score mémoire 9.055/10 — sources ACCELERATION — MEMORY_ONLY
- LISTA-EUR — MEMORY_24H — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 7.372/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 6.737/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.540/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 6.325/10 — sources ACCELERATION — MEMORY_ONLY
- AI-EUR — ACTIVE_NOW — score mémoire 6.231/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- TREAD-EUR — ACTIVE_NOW — score mémoire 6.158/10 — sources DECISION_LAYER — WATCH_ONLY
- SKY-EUR — MEMORY_24H — score mémoire 5.906/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- BIGTIME-EUR +83.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +18.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MANTRA-EUR +17.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SSV-EUR +12.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +10.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAXP-EUR +9.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +8.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOSO-EUR +7.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MOVE-EUR +7.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +6.80% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
