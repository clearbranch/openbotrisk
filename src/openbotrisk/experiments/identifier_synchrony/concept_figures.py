"""Illustrative concept figures for the methodology concepts page.

These are deliberately tiny, hand-built toy graphs, NOT derived from the
synthetic experiment data. Their only job is to make two abstract steps
concrete for a reader:

1. projection -- turning an account<->identifier bipartite graph into an
   account<->account graph, including how one shared identifier can *bridge*
   two otherwise-separate groups;
2. pruning + inverse-frequency weighting -- why a promiscuous identifier is
   dropped and why a rare shared identifier produces a strong edge;
3. two pipeline diagrams (one per method) showing each method as a failure-
   driven progression: simple idea -> failure -> the layer that fixes it.

Run:
    python concept_figures.py
"""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

OUT = Path(".")

ACCOUNT_C = "#4878a8"
IDENT_C = "#dd8452"
BRIDGE_C = "#c44e52"
GROUP1_C = "#4878a8"
GROUP2_C = "#6acc64"
PRUNE_C = "#b8b8b8"


def fig_projection(path: Path) -> None:
    """Bipartite graph and its account-account projection, side by side."""

    # Two small groups, each sharing one IP; one card bridges them.
    accounts = ["a1", "a2", "a3", "a4", "a5"]
    edges_bip = [
        ("a1", "IP_1"), ("a2", "IP_1"), ("a3", "IP_1"),   # group 1 shares IP_1
        ("a3", "Card_1"), ("a4", "Card_1"),               # bridge: shared card
        ("a4", "IP_2"), ("a5", "IP_2"),                   # group 2 shares IP_2
    ]
    idents = ["IP_1", "Card_1", "IP_2"]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 5.5))

    # --- left: bipartite ---
    B = nx.Graph()
    B.add_nodes_from(accounts, kind="account")
    B.add_nodes_from(idents, kind="ident")
    B.add_edges_from(edges_bip)
    # a1..a5 top-to-bottom so edges to IP_1/Card_1/IP_2 don't criss-cross
    pos_acc = {a: (0, (len(accounts) - 1 - i)) for i, a in enumerate(accounts)}
    pos_id = {"IP_1": (2, 3.6), "Card_1": (2, 2.2), "IP_2": (2, 0.8)}
    pos = {**pos_acc, **pos_id}

    nx.draw_networkx_edges(B, pos, ax=axL, edge_color="#cccccc", width=1.6)
    nx.draw_networkx_nodes(
        B, pos, nodelist=accounts, node_color=ACCOUNT_C, node_shape="o",
        node_size=900, ax=axL,
    )
    nx.draw_networkx_nodes(
        B, pos, nodelist=idents, node_color=IDENT_C, node_shape="s",
        node_size=1500, ax=axL,
    )
    nx.draw_networkx_labels(B, pos, ax=axL, font_size=9, font_color="white")
    axL.set_title(
        "Bipartite graph\naccounts (circles) linked only to the identifiers "
        "(squares) they used",
        fontsize=11,
    )
    axL.text(0, -0.7, "accounts", ha="center", fontsize=9, color="#555")
    axL.text(2, -0.7, "identifiers", ha="center", fontsize=9, color="#555")
    axL.axis("off")
    axL.set_ylim(-1.1, 4.4)

    # --- right: projection ---
    P = nx.Graph()
    P.add_nodes_from(accounts)
    # edges within each group (from shared IP) + the bridge (from shared card)
    proj_edges = [
        ("a1", "a2"), ("a1", "a3"), ("a2", "a3"),   # IP_1 clique
        ("a4", "a5"),                                # IP_2
    ]
    bridge_edges = [("a3", "a4")]                    # Card_1 bridge
    P.add_edges_from(proj_edges + bridge_edges)
    posP = nx.spring_layout(P, seed=3, k=1.2)

    nx.draw_networkx_edges(P, posP, edgelist=proj_edges, ax=axR,
                           edge_color="#999999", width=2.2)
    nx.draw_networkx_edges(P, posP, edgelist=bridge_edges, ax=axR,
                           edge_color=BRIDGE_C, width=2.6, style="dashed")
    colours = [GROUP1_C, GROUP1_C, GROUP1_C, GROUP2_C, GROUP2_C]
    nx.draw_networkx_nodes(P, posP, node_color=colours, node_size=900, ax=axR)
    nx.draw_networkx_labels(P, posP, ax=axR, font_size=9, font_color="white")
    # label the bridge
    bx = (posP["a3"][0] + posP["a4"][0]) / 2
    by = (posP["a3"][1] + posP["a4"][1]) / 2
    axR.text(bx, by + 0.12, "shared card\n(bridge)", color=BRIDGE_C,
             fontsize=8, ha="center", va="bottom")
    axR.set_title(
        "Projection: account-account graph\nidentifiers dropped; one shared "
        "card merges two groups",
        fontsize=11,
    )
    axR.axis("off")

    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)


def fig_prune_weight(path: Path) -> None:
    """Raw projection vs after pruning a promiscuous identifier and weighting."""

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Scenario: 6 unrelated accounts all behind one shared public IP (h1..h6),
    # plus a real pair (r1, r2) that share a rare card.
    hub = [f"h{i}" for i in range(1, 7)]
    pair = ["r1", "r2"]

    # --- left: raw projection (every shared identifier => an edge) ---
    L = nx.Graph()
    L.add_nodes_from(hub + pair)
    # promiscuous IP: clique across all hub accounts
    hub_edges = [(u, v) for i, u in enumerate(hub) for v in hub[i + 1:]]
    L.add_edges_from(hub_edges)
    L.add_edge("r1", "r2")
    posL = nx.spring_layout(L, seed=7, k=0.9)
    nx.draw_networkx_edges(L, posL, edgelist=hub_edges, ax=axL,
                           edge_color="#cccccc", width=1.2)
    nx.draw_networkx_edges(L, posL, edgelist=[("r1", "r2")], ax=axL,
                           edge_color="#555", width=2.0)
    nx.draw_networkx_nodes(L, posL, nodelist=hub, node_color=PRUNE_C,
                           node_size=650, ax=axL)
    nx.draw_networkx_nodes(L, posL, nodelist=pair, node_color=ACCOUNT_C,
                           node_size=650, ax=axL)
    nx.draw_networkx_labels(L, posL, ax=axL, font_size=8, font_color="white")
    axL.set_title(
        "Raw projection\none public IP shared by 6 strangers -> 15 edges\n"
        "(a benign 'hairball')",
        fontsize=11,
    )
    axL.axis("off")

    # --- right: after pruning + weighting ---
    R = nx.Graph()
    R.add_nodes_from(hub + pair)
    R.add_edge("r1", "r2", weight=3.0)  # rare shared card: strong
    posR = dict(posL)
    nx.draw_networkx_edges(R, posR, edgelist=[("r1", "r2")], ax=axR,
                           edge_color="#555", width=5.0)
    nx.draw_networkx_nodes(R, posR, nodelist=hub, node_color=PRUNE_C,
                           node_size=650, ax=axR, alpha=0.35)
    nx.draw_networkx_nodes(R, posR, nodelist=pair, node_color=ACCOUNT_C,
                           node_size=650, ax=axR)
    nx.draw_networkx_labels(R, posR, ax=axR, font_size=8, font_color="white")
    bx = (posR["r1"][0] + posR["r2"][0]) / 2
    by = (posR["r1"][1] + posR["r2"][1]) / 2
    axR.text(bx, by + 0.10, "rare shared card\n= strong edge", color="#333",
             fontsize=8, ha="center", va="bottom")
    axR.text(posR["h3"][0], posR["h3"][1] - 0.28,
             "public IP pruned\n(degree > cap)", color="#999",
             fontsize=8, ha="center", va="top")
    axR.set_title(
        "After pruning + weighting\npromiscuous IP removed; the one rare, "
        "discriminative link survives",
        fontsize=11,
    )
    axR.axis("off")

    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)


def _pipeline(path: Path, title: str, stages: list[str],
              problems: dict[int, str], arrow_labels: dict[int, str]) -> None:
    """Draw a vertical stage flow with failure annotations beside the gaps.

    Args:
        path: PNG output path.
        title: Figure title.
        stages: Box labels, top to bottom.
        problems: ``{gap_index: text}`` -- the failure that forces stage
            ``gap_index + 1``, drawn in red beside the gap below box
            ``gap_index``.
        arrow_labels: ``{gap_index: text}`` -- neutral labels for gaps with no
            failure (e.g. "find groups").
    """

    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

    n = len(stages)
    fig, ax = plt.subplots(figsize=(8.4, 1.55 * n + 0.6))
    box_x, box_w, box_h = 0.30, 0.40, 0.62
    gap = 1.0
    ys = [(n - 1 - i) * gap for i in range(n)]

    for i, (label, y) in enumerate(zip(stages, ys, strict=True)):
        last = i == n - 1
        ax.add_patch(FancyBboxPatch(
            (box_x, y - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=1.4,
            edgecolor="#2a2a2a" if not last else "#c44e52",
            facecolor="#eef2f6" if not last else "#fbe9ea",
        ))
        ax.text(box_x + box_w / 2, y, label, ha="center", va="center",
                fontsize=10.5, color="#1a1a1a")

    for i in range(n - 1):
        y0, y1 = ys[i] - box_h / 2, ys[i + 1] + box_h / 2
        ax.add_patch(FancyArrowPatch(
            (box_x + box_w / 2, y0), (box_x + box_w / 2, y1),
            arrowstyle="-|>", mutation_scale=16, lw=1.4, color="#666"))
        if i in problems:
            ax.annotate(
                "problem:\n" + problems[i],
                xy=(box_x + box_w, (y0 + y1) / 2),
                xytext=(box_x + box_w + 0.06, (y0 + y1) / 2),
                ha="left", va="center", fontsize=9, color="#c44e52",
                arrowprops=dict(arrowstyle="-", color="#c44e52", lw=0.8))
        elif i in arrow_labels:
            ax.text(box_x + box_w / 2 + 0.012, (y0 + y1) / 2, arrow_labels[i],
                    ha="left", va="center", fontsize=8.5, color="#888",
                    style="italic")

    ax.set_title(title, fontsize=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.7, (n - 1) * gap + 0.7)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)


def fig_pipeline_m1(path: Path) -> None:
    """Method 1 as a failure-driven evolution."""

    _pipeline(
        path,
        "Method 1: each layer answers a failure of the one above",
        stages=[
            "Link accounts that share an identifier",
            "Prune promiscuous identifiers",
            "Weight links by type & rarity",
            "Connected components",
            "Split with community detection",
            "Score clusters on behaviour",
            "Flag suspicious clusters only",
        ],
        problems={
            0: "a public IP links\n120 strangers",
            1: "a shared card is worth\nmore than a shared IP",
            3: "one bridge merges\ntwo real rings",
            4: "a benign office is\na perfect cluster",
        },
        arrow_labels={2: "find groups", 5: "judge them"},
    )


def fig_pipeline_m2(path: Path) -> None:
    """Method 2 as a failure-driven evolution."""

    _pipeline(
        path,
        "Method 2: each layer answers a failure of the one above",
        stages=[
            "Bucket events into (action, target, time) tokens",
            "Link accounts that share a token",
            "Drop too-popular tokens",
            "Score overlap with Jaccard (relative)",
            "Connected components = synchrony clusters",
        ],
        problems={
            1: "a flash sale makes\nthousands co-occur",
            2: "busy accounts share\ntokens by chance",
        },
        arrow_labels={0: "co-occurrence", 3: "keep strong links"},
    )


def main(out_dir: Path = OUT) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_projection(out_dir / "concept_projection.png")
    fig_prune_weight(out_dir / "concept_prune_weight.png")
    fig_pipeline_m1(out_dir / "concept_pipeline_m1.png")
    fig_pipeline_m2(out_dir / "concept_pipeline_m2.png")
    print("wrote concept_projection.png, concept_prune_weight.png, "
          "concept_pipeline_m1.png, concept_pipeline_m2.png")


if __name__ == "__main__":
    main()
