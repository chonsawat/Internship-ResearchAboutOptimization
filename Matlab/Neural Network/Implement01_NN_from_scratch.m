data = [0 0;
        0 1;
        1 0;
        1 1];
label = [0;
         1;
         1;
         0];
X = repmat(data, 5, 1);
y = repmat(label, 5, 1);

wh = rand(size(X));
bh = rand(size(X, 1), 1);
zh = sum(X.*wh, 2) + bh;

wh_o = rand(size(zh));
bh_o = rand(size(zh, 1), 1);
zh_o = sum(zh.*wh_o, 2) + bh_o;


1 / (1 + exp(-X));
