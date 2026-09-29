# Verify Before Delivery

Before any non-trivial artifact is called done, pass it to the verifier in fresh context.

1. Give the verifier the finished artifact plus its acceptance criteria: never the producing agent's reasoning or draft history. The artifact must stand alone.
2. When the artifact ships with an inputs file and a compute script (finance artifacts do), run the script yourself and include its output in the dispatch. The verifier compares; it does not execute.
3. When the artifact rests on web sources, include the load-bearing excerpts (the exact sentences the artifact relies on) in the dispatch. The verifier has no web access by design; without an excerpt it can only mark a web-cited claim SOURCE UNREACHABLE.
4. Treat CONFIRMED findings as fixes. Treat PLAUSIBLE findings as judgment calls for the owner.
5. "No confirmed issues" is a valid, expected outcome. Do not invent changes to justify the review.

Skip only for trivial or throwaway work.
