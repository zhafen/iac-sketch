# What is data?

# What is an entity?

# Why is there no perfect formulation of the data for a given entity?


# Where does one entity end and another begin?

# Key information

1. The universe is composed of atoms, and follows the laws of physics.
2. Humans are a product of evolution.

From point (1) we know that a list of atom coordinates and states (the "particle data") is probably the best possible approximation to what reality really is. So why can't we just use that?

As products of evolution, the behavior of humans was shaped s.t. behaviors that did not promote survival lasted more briefly (I need to study biology to get this right).  Or something like that. What I think we can confidently say is that human actions often occur with a goal in mind. We want to eat, sleep, etc. To accomplish our goals, we need information. Where is the door, and where is the wall? What food is edible and what food will cause sickness. We also don't necessarily have goals. People often just exist,
and react to what happens.

Let's assume overall that we gather data for the sake of doing something, and that that data guides our actions.

With that in mind, the particle data doesn't work for at least two reasons:
1. We don't know the values.
2. Even if we did, performing a calculation to know what you need to know to accomplish your goals can be very laborious given the particle data.

For something as simple as "can we lift this", the particle data would need to be summed and compared to what we can lift. It's much harder with "is this safe to eat", etc.

Instead, having the key information prepared that will help us make decisions is the superior option. If we already have the weight recorded, perhaps from empirically weighing it, we could just use that to guide our decisions.

# Even if the particle data formulation doesn't work, can there be a formulation that's perfect for all decision making?

For a data formulation to be valid for a given objective, we need to (a) be able to calculate the key data needed to guide the decision, (b) the calculation can't take forever.

A very simple formulation is Entity-Attribute-Value. Why can't we just use that for everything? If the answer we want to know is already a given attribute, and there aren't an insanse number of attributes, then that should work. However, what if we don't know the answer? Then we have to calculate it based on the attributes. Calculating the value requires collecting the relevant data from the full EAV table, and then arranging it in a form where the calculation can be done. For example, if it's computationally intensive we need to gather all the data and put it into an array so we can efficiently loop over it. Or if we want to summarize a visual pattern we need to plot it all. Different data formulations are more efficient or required for different purposes.

# Okay, so different data formulations are useful for different purposes. Then what about a data formulation that's intended to help make decisions about system design?

Well, how does system design work? What is the process?

1. List the requirements. Typically it's a task to achieve.
2. List relevant information we suspect will help us.
3. Write instructions to complete the task.
4. Test the instructions, and find out what does and doesn't work.
5. Modify the instructions.
6. Repeat 4 and 5.

# What about a data formulation for documentation?

What is documentation? It contains
- the raw information for how a requirement is met
- necessary procedure to meet the requirement
- necessary information to update the procedure under a change in requirements
- necessary information to fix something if it breaks
- a way to find the relevant documentation for something

# What data formulation will we use?

Currently I'm leaning towards an Entity-Component-System-like yaml formulation for defining infrastructure. For storing the data, I was thinking about having it stored as relational data. So we would need a converter from ECS-yaml to relational data. I've looked around for a little bit, but I haven't found anything trhat uses this formulation. The reason I'm leaning towards it is that makes it really easy to describe arbitrary objects. I *think* in this framework that each component instance is a resource.

For uniquely identifying component instances I was going to have the entity they are associated with as well as an index counting which number component they are for that entity. So the ID for a given component is (entity_id,entity_index), and every component table would have that.

All this said and done, why do I want the infrastructure saved in 3NF? What benefit does that provide? Why not keep it as yaml?
Well, for one, I definitely want the user-defined tables to be created, so they can be used.