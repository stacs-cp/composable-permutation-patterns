
echo "" > combined.essence

cat ../pattern-type/classic-containment.essence | grep '^given length' >> combined.essence
cat ../pattern-type/classic-containment.essence | grep '^find perm' >> combined.essence
cat ../pattern-type/mesh-containment.essence | grep '^find permPadded' >> combined.essence


printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/classic-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/classic-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/vincular-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/vincular-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/bivincular-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/bivincular-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/mesh-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/mesh-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/boxed-mesh-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/boxed-mesh-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/consecutive-containment.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../pattern-type/consecutive-avoidance.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence

printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/simple.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_simple/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/block-wise-simple.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_block_wise_simple/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/plus-decomposable.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_plus_decomposable/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/minus-decomposable.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_mins_decomposable/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/involution.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_involution/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/derangement.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_derangement/g' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../permutation-property/non-derangement.essence | grep -v '^given length' | grep -v '^find perm' | sed 's/turnedOn/prop_non_derangement/g' >> combined.essence


printf "\n\n\n\n" >> combined.essence ; cat ../stats/inversion-count.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../stats/descents-count.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../stats/ascents-count.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../stats/excedance-count.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence
printf "\n\n\n\n" >> combined.essence ; cat ../stats/major-index.essence | grep -v '^given length' | grep -v '^find perm' >> combined.essence

