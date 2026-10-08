# WALLET — collecte des carnets et transactions des positions détenues

## Fonctionnement

Le workflow `.github/workflows/private_wallet_refresh.yml` crée d'abord
`wallet_private_summary.json` depuis les soldes Bitvavo **en lecture seule**.
`scripts/enrich_private_wallet.py` charge ensuite ce résumé, découvre ses
`positions[*].market`, et interroge uniquement les API publiques Bitvavo
`/ticker/24h`, `/{market}/book?depth=100` et `/{market}/trades?limit=100`.

Aucune position détenue n'est exclue au motif qu'elle est absente de
`decision_watchlist.json`, du scanner Solaire, ou d'un classement V3/V4.
Chaque position reçoit `execution_evidence`, même si les observations sont
impossibles (`PARTIAL`, `UNAVAILABLE` ou `NOT_OBSERVED`). Les opérations
sont soumises à un budget de 90 secondes et 30 actifs par cycle :
l'absence de collecte est explicitement indiquée, jamais assimilée à un
carnet vide ni à une absence de détention.

## Mesures par position

- Carnet jusqu'à **100 bids + 100 asks**, meilleur bid/ask et tailles,
  spread recalculé depuis le **même carnet** et profondeur notionnelle
  à ±0,25 %, ±0,5 % et ±1 %.
- Jusqu'à **100 transactions publiques**, horodatage et prix du dernier
  échange, VWAP, volumes agressifs acheteur/vendeur, part acheteuse et
  durée de la fenêtre couverte par l'échantillon.
- Volume EUR 24 h, variation 24 h et dernier cours du ticker public.
- Estimation du prix moyen de vente **de la quantité réellement détenue**
  sur le carnet observé ; simulations distinctes d'achat et de vente de
  50/100/150 EUR, sans déduction de frais ni ordre exécuté.
- Horodatage propre du ticker, du carnet et des trades ; âges au moment de
  l'écriture. Une collecte de plus de 90 secondes ou un dernier trade
  datant de plus de 15 minutes ne reçoit **pas** le statut OK.

Les données sont des photographies ponctuelles, **pas** un historique des
ordres exécutés et non exécutés. Un gros mur bid peut être retiré ; un
échantillon de 100 trades ne prouve pas une tendance durable. Les simulations
de slippage ne tiennent pas compte de la profondeur future ni des frais réels.

## Confidentialité, accès et non-régression

Le fichier enrichi est publié **uniquement comme artifact Actions du workflow
privé existant**, sous le même nom `private-wallet-summary-…`. Il n'est
jamais ajouté à Git, ni à `execution_snapshot.json`, ni aux fichiers publics
de détection. Les logs n'affichent plus les montants et les symboles du wallet
dans l'étape de validation.

**Attention :** ce workflow est dans un dépôt GitHub public. Les artifacts
Actions ne doivent pas être considérés comme un coffre-fort cryptographique :
leur accès est régi par les permissions de consultation GitHub. Le résumé
préexistant expose déjà le portefeuille dans ce canal ; cette modification ne
rajoute pas de nouvelle destination, mais n'élimine pas ce risque existant.

Aucun endpoint Bitvavo privé supplémentaire, aucun ordre, aucun email et
aucune modification de la politique stop-loss. Le scanner public, les
fichiers utilisés pour ses alertes d'achat et `execution_snapshot.json`
restent indépendants. Les champs de freshness doivent être recontrôlés au
moment de chaque réponse utilisateur ; un artifact de la nuit ne peut être
présenté comme une cotation instantanée en journée.
