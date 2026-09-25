class Solution {
    private String expr;
    private int pos;

    public List<String> braceExpansionII(String expression) {
        this.expr = expression;
        this.pos = 0;
        Set<String> result = parseExpr();
        List<String> answer = new ArrayList<>(result);
        Collections.sort(answer);
        return answer;
    }

    private Set<String> parseExpr() {
        Set<String> result = new HashSet<>();
        result.addAll(parseTerm());
        while (pos < expr.length() && expr.charAt(pos) == ',') {
            pos++;
            result.addAll(parseTerm());
        }
        return result;
    }

    private Set<String> parseTerm() {
        List<Set<String>> factors = new ArrayList<>();
        while (pos < expr.length() && expr.charAt(pos) != ',' && expr.charAt(pos) != '}') {
            factors.add(parseFactor());
        }
        return concatFactors(factors);
    }

    private Set<String> parseFactor() {
        if (expr.charAt(pos) == '{') {
            pos++;
            Set<String> result = parseExpr();
            pos++;
            return result;
        } else {
            int start = pos;
            while (pos < expr.length() && Character.isLowerCase(expr.charAt(pos))) {
                pos++;
            }
            Set<String> result = new HashSet<>();
            result.add(expr.substring(start, pos));
            return result;
        }
    }

    private Set<String> concatFactors(List<Set<String>> factors) {
        Set<String> result = new HashSet<>();
        result.add("");
        for (Set<String> factor : factors) {
            Set<String> temp = new HashSet<>();
            for (String prefix : result) {
                for (String word : factor) {
                    temp.add(prefix + word);
                }
            }
            result = temp;
        }
        return result;
    }
}